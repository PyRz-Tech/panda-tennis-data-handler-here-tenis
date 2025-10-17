import os

from dotenv import load_dotenv


load_dotenv()


def get_api_key():
	api_key = os.getenv("API_KEY")
	if api_key:
		print(f"succes get api key: {api_key}")
		return api_key
	else:
		print("faild get api key")
		return None
