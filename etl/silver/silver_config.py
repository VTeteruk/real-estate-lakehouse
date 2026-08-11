SILVER_SCHEMA = "silver"
SILVER_TABLES = ["bazos", "rapidapi"]

DEDUP_CONFIG = {
    "price_range": 50,
    "distance_threshold": 5,
    "group_keys": ["location_city", "price_amount"],
}
