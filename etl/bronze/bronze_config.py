BASE_PATH = "/Volumes/real_estate_elt/default/bronze_volume"

INGESTION_CONFIG = [
    {
        "source": "bazos",
        "path": "{BASE_PATH}/bazos/*/*/{TODAY}/listings.json",
        "table": "bazos"
    },
    {
        "source": "rapidapi",
        "path": "{BASE_PATH}/rapidapi/{TODAY}/listings.json",
        "table": "rapidapi"
    }
]
