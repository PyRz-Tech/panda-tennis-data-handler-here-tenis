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