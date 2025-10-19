
from src.api_client import GetInfoApi

if __name__ == "__main__":
    api = GetInfoApi()
    df = api.save_to_dataframe()
    if df is not None:
        print(df.head())