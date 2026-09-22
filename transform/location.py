"""Helpers for extracting and normalizing job-location fields."""

from __future__ import annotations

import re
import unicodedata


def _comparison_key(value: str) -> str:
    """Return a case- and accent-insensitive key for location aliases."""
    value = unicodedata.normalize("NFD", value.casefold())
    value = "".join(char for char in value if not unicodedata.combining(char))
    value = value.replace("đ", "d")
    return re.sub(r"[^a-z0-9]", "", value)


_CITY_ALIASES = {
    "hanoi": "Hà Nội",
    "tphanoi": "Hà Nội",
    "hochiminh": "Hồ Chí Minh",
    "tphochiminh": "Hồ Chí Minh",
    "tphcm": "Hồ Chí Minh",
    "hcm": "Hồ Chí Minh",
    "saigon": "Hồ Chí Minh",
    "danang": "Đà Nẵng",
    "tpdanang": "Đà Nẵng",
    "haiphong": "Hải Phòng",
    "tphaiphong": "Hải Phòng",
    "cantho": "Cần Thơ",
    "tpcantho": "Cần Thơ",
    "hue": "Huế",
    "tphue": "Huế",
}


def extract_city(location_raw: str | None) -> str | None:
    """Extract the city label, conventionally placed before the first colon."""
    if not isinstance(location_raw, str):
        return None

    city = location_raw.split(":", maxsplit=1)[0].strip(" ,:-")
    return city or None


def normalize_city(city: str | None) -> str | None:
    """Normalize common Vietnamese city aliases without discarding unknown names."""
    if not isinstance(city, str):
        return None

    city = re.sub(r"\s+", " ", city).strip(" ,:-")
    city = re.sub(r"^(?:thành phố|tp\.?|tỉnh)\s*", "", city, flags=re.IGNORECASE)
    city = city.strip()
    if not city:
        return None

    return _CITY_ALIASES.get(_comparison_key(city), city)


def extract_address(location_raw: str | None) -> str | None:
    """Extract the address portion after the first colon, if one is present."""
    if not isinstance(location_raw, str) or ":" not in location_raw:
        return None

    address = location_raw.split(":", maxsplit=1)[1].strip(" ,:-")
    return address or None


def normalize_location(location_raw: str | None) -> tuple[str | None, str | None]:
    """Return ``(city, address)`` from a raw job-location label.

    This function coordinates city extraction, city normalization, and address
    extraction while keeping each parsing step independently reusable.
    """
    return normalize_city(extract_city(location_raw)), extract_address(location_raw)


def transform_location(location_raw: str | None) -> tuple[str | None, str | None]:
    """Backward-compatible name for :func:`normalize_location`."""
    return normalize_location(location_raw)
