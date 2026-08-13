from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional

@dataclass
class RealEstateListing:
    listing_id: str
    source: str
    source_url: str
    property_type: str
    transaction_type: str
    title: str
    description: str
    price: str
    location_city: Optional[str] = None
    location_zip: Optional[str] = None
    posted_date: Optional[str] = None
    images: list[str] = field(default_factory=list)
    rooms_count: Optional[str] = None
    area: Optional[str] = None
    scraped_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
