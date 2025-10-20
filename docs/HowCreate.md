## How I Threw This Project Together

Yo, here’s the lowdown on how I built this project. The goal was to snag some data from a REST API, clean it up, and get it ready for machine learning (ML) action. I wanted it simple, modular, and no hardcoding nonsense to make my life easier later. Here’s how it all came together.

### Step 1: Mapping It Out
First, I sketched a diagram to figure out what the heck this program’s supposed to do. The flow’s like this:
- **Ping a REST API** to grab data from a site.
- **Send a request** to pull the data.
- **Turn the response into JSON**.
- **Make it a Pandas DataFrame** for easy cleaning and ML prep.
- **Save that DataFrame to a CSV file**.

That’s the game plan, and I turned it into a visual diagram to keep things crystal clear:

```mermaid
graph TD
    A[REST API] -->|Request| B[Python: requests]
    B -->|JSON Response| C[JSON Data]
    C -->|Convert| D[Pandas DataFrame]
    D -->|Save| E[Output.csv]
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
    style D fill:#fbf,stroke:#333,stroke-width:2px
    style E fill:#ffb,stroke:#333,stroke-width:2px

Step 2: Keeping It Modular
To avoid a code mess, I broke the project into bite-sized pieces. Each part’s got one job, and I steered clear of hardcoding to make tweaks and testing a breeze. Here’s the breakdown:

One module for API key setup.
One for fetching API data and turning it into JSON.
One for processing JSON into a Pandas DataFrame.
A helper module with utility functions like grabbing the API key, making requests, and saving to CSV.

Oh, and pro tip: logging is your best friend in projects like this. Simple, clear logs save your butt when debugging, so I added some to track what’s going on.
Project Structure
I laid out the project’s folder structure to keep it tidy. Here’s the tree:
api_tennis_project/
├── config/
│   ├── config.py
│   ├── __init__.py
├── src/
│   ├── api_client.py
│   ├── data_processor.py
│   ├── utils.py
│   ├── __init__.py
├── run.py
├── requirements.txt
├── tournament/
├── docs/
├── .env


config/: Where the API key setup lives.
src/: Home for the main code—API calls, data processing, and utilities.
run.py: The script that ties it all together.
requirements.txt: Lists the libraries we’re using.
tournament/: Folder for output files like the CSV.
docs/: For project docs (like this one!).
.env: Keeps sensitive stuff like the API key safe.

Libraries I’m Rocking
Kept it lean with these Python libraries:

requests: For hitting the API and grabbing data.
pandas: For turning JSON into DataFrames and cleaning it up.
python-dotenv: For safely pulling the API key from .env.

Setting Up the .env File
I’m using a REST API from api-tennis.com (you can score a free API key there!). To keep the key secure, I set up a .env file like this:
API_KEY=******************************

To use it, install python-dotenv:
pip install python-dotenv

Then, I wrote a helper function in src/utils.py to snag the API key from .env:
# src/utils.py
from os import getenv
from dotenv import load_dotenv
import logging

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(encoding='utf-8', level=logging.INFO)

def get_api_key():
    logger.info("try get api key")
    if api_key:
        logger.info("success get api key: ***************")
        return api_key
    else:
        logger.warning("faild get api key")
        return None

I kept it simple but threw in try/except for easy debugging. Could’ve loaded getenv locally to lighten the load, but this setup’s better for tweaking and catching errors.
Setting Up the Config
In config/config.py, I grab the API key with that helper function:
# config/config.py
from src.utils import get_api_key

API_KEY = get_api_key()

Short, sweet, and no hardcoding—easy to change later.
Hitting the API
For grabbing data from the API and turning it into JSON, I set up src/api_client.py. To keep things clean, I made a reusable request function in src/utils.py:
# src/utils.py (add to existing file)
import requests

def make_api_request(url, params=None, headers=None):
    try:
        logger.info("try make api request")
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            logger.info("successfull request and status code is 200")
            return response.json()
        else:
            logger.warning(f"request failed with status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Error occurred: {e}")
        return None

Then, I use it in src/api_client.py to keep things DRY:
# src/api_client.py
from config.config import API_KEY
from src.utils import make_api_request
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(encoding='utf-8', level=logging.INFO)

class GetApiClient:
    def __init__(self):
        self.api_key = API_KEY
        self.url = f"https://api.api-tennis.com/tennis/?method=get_tournaments&APIkey={self.api_key}"

    def fetch_tournament_data(self):
        logger.info("try to fetch tournament data")
        return make_api_request(self.url)

Logging’s in there to track what’s happening, making debugging a walk in the park.
Turning JSON into a Pandas DataFrame
Next, I needed to whip that JSON into a Pandas DataFrame for cleaning and ML prep. This goes down in src/data_processor.py:
# src/data_processor.py
import pandas as pd
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(encoding='utf-8', level=logging.INFO)

class DataProcessor:
    @staticmethod
    def process_tournament_data(json_data):
        try:
            logger.info("try process tournament data")
            if not json_data or json_data.get("success") != 1:
                logger.warning("Invalid or unsuccessful API response")
                return None
            logger.info("passed validation (valid-json-data or json_data_success != 1)")
            result = json_data.get("result", [])
            if not result:
                logger.warning("No tournament data found")
                return None
            logger.info("tournament data found -> converting to pandas.DataFrame")
            df = pd.DataFrame(result)
            return df
        except Exception as e:
            logger.error(f"Error proccessing data: {e}")
            return None

Used @staticmethod since this function doesn’t need class or instance data—just a clean way to make a DataFrame.
Saving to CSV
Saving the DataFrame to a CSV is something I might reuse, so I stuck it in src/utils.py:
# src/utils.py (add to existing file)
def save_dataframe_to_csv(df, output_file="tournament/output.csv"):
    try:
        logger.info("try save dataframe to csv")
        if df is None or df.empty:
            logger.warning("No data to save")
            return False
        df.to_csv(output_file, index=False)
        logger.info(f"Data saved successfully to {output_file}")
        return True
    except Exception as e:
        logger.error(f"Error saving Dataframe: {e}")
        return False

This checks if the DataFrame’s legit, saves it, and logs the action.
Gluing It All Together
Finally, run.py brings it all together:
# run.py
from src.api_client import GetApiClient
from src.data_processor import DataProcessor
from src.utils import save_dataframe_to_csv
if __name__ == "__main__":
    request_data = GetApiClient()
    json_data = request_data.fetch_tournament_data()
    df = DataProcessor.process_tournament_data(json_data=json_data)
    save_dataframe_to_csv(df=df)

    # show 5 info in terminal
    print(df)

Libraries Needed
Toss these into requirements.txt:
requests
pandas
python-dotenv

Wrapping Up the Plan
This was my first crack at the project. I started with a diagram to nail the flow, broke it into modular chunks to keep it clean, and dodged hardcoding to make testing and tweaks easier. Logging’s a lifesaver for tracking what’s up. The code’s a solid base, but it could use some extra love—like beefier error handling or more logs—to be bulletproof. This doc’s all about showing how I think when I’m coding something like this.```
