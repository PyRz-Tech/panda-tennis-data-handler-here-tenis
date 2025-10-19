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