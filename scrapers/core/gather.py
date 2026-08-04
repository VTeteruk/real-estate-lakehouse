import json
import logging
from collections import defaultdict
from dataclasses import asdict
from datetime import date

import sys, os
sys.path.append(os.path.abspath(".."))

from core.schemas import RealEstateListing


logger = logging.getLogger(__name__)


class Gather:
    def __init__(self, source: str, is_debug: bool = False):
        self.source = source
        self.is_debug = is_debug
        self._items: list[RealEstateListing] = []

    def push(self, listing: RealEstateListing) -> None:
        self._items.append(listing)

    @property
    def pushed_cnt(self) -> int:
        return len(self._items)

    def push_to_bronze(self) -> None:
        if self.is_debug:
            logger.info(f"[DEBUG] Gathered {self.pushed_cnt} listings, first 5:")
            for item in self._items[:5]:
                print(json.dumps(asdict(item), indent=2, ensure_ascii=False))
            return

        groups: dict[tuple[str, str], list[RealEstateListing]] = defaultdict(list)
        for item in self._items:
            groups[(item.property_type, item.transaction_type)].append(item)

        for (property_type, transaction_type), items in groups.items():
            payload = [asdict(item) for item in items]
            path = (
                f"bronze/{self.source}/{property_type}/{transaction_type}"
                f"/{date.today().isoformat()}/listings.json"
            )
            # TODO: push to Azure
            
            logger.info(f"Pushed {len(items)} listings to {path}")
