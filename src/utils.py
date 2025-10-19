import pandas as pd
import requests
import os
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(encoding='utf-8', level=logging.INFO)

load_dotenv()
api_key = os.getenv("API_KEY")

def get_api_key():
    logger.info("try get api key")
    if api_key:
        logger.info("success get api key: ***************")
        return api_key
    else:
        logger.warning("faild get api key")
        return None

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