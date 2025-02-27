import sys
import requests
import json
from config import CurrentConfig
from app.services.redis_service import get_redis_client
from app.utils import log_info, log_error

TAX_API_BASE_URL = CurrentConfig.TAX_API_BASE_URL
MAX_RETRIES = CurrentConfig.MAX_RETRIES

def fetch_tax_brackets(tax_year):
    """Fetch tax brackets for a specific year from the tax calculator API"""
    cache_key = f"tax_brackets:{tax_year}"
    redis_client = get_redis_client()

    # Fetch tax brackets from the API
    retries = 0
    while retries < MAX_RETRIES:
        try:
            response = requests.get(f"{TAX_API_BASE_URL}{tax_year}")
            response.raise_for_status()
            tax_data = response.json()

            # Cache the tax brackets in Redis for forever
            redis_client.set(cache_key, json.dumps(tax_data))
            log_info(f"Fetched tax brackets for {tax_year} from API and cached in Redis")
            return tax_data
        except requests.exceptions.RequestException as e:
            retries += 1
            log_error(f"Failed to fetch tax brackets: {e}")
    
    log_error(f"Failed to fetch tax brackets after {MAX_RETRIES} retries")
    sys.exit(1)

def cache_all_tax_brackets():
    """Cache tax brackets for the years 2019-2022"""
    for year in [2019, 2020, 2021, 2022]:
        fetch_tax_brackets(year)


