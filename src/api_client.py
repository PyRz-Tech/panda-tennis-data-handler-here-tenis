import requests
import json
from config.config import get_api_key
import pandas as pd
class GetInfoApi():
	def __init__(self):
		self.api_key = get_api_key()
		self.url = f"https://api.api-tennis.com/tennis/?method=get_tournaments&APIkey={self.api_key}"
	def response_from_site_tenis_api(self):
		try:
			response = requests.get(self.url)
			if response.status_code == 200:
				return True, response.json()
			else:
				return False, response.status_code

		except requests.exceptions.RequestException as e:
			print(f"Error occured: {e}")
			return False, str(e)

	def get_json_response(self):
			success, data = self.response_from_site_tenis_api()
			if success:
				return data
			else:
				print(f"Failed to fetch data: {data}")
				return None

	def save_to_dataframe(self):
		data = self.get_json_response()
		if data and data.get("success") == 1:
			try:
				result = data.get("result", [])
				df = pd.DataFrame(result)
				df.to_csv("../tenis_tournaments.csv", index=False)
				return df
			except Exception as e:
				print(f"Error converting to DataFrame: {e}")
				return None
		return None
