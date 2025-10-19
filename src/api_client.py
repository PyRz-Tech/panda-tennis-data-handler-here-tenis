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