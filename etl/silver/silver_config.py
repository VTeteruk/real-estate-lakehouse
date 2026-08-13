SILVER_SCHEMA = "silver"
SILVER_TABLES = ["bazos", "rapidapi"]

DEDUP_CONFIG = {
    "price_range": 50,
    "distance_threshold": 5,
    "group_keys": ["location_city", "price_amount"],
}

SILVER_COLUMNS = [
    "listing_id", "title", "price_amount", "currency", "rooms_count", "area",
    "location_city", "location_zip", "property_type", "transaction_type",
    "images", "description", "source", "source_url", "scraped_at", "posted_date"
]
