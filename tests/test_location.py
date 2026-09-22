import pytest

from transform.location import (
    extract_address,
    extract_city,
    normalize_city,
    normalize_location,
    transform_location,
)


@pytest.mark.parametrize(
    ("location_raw", "expected"),
    [
        ("Hà Nội : 204 Nguyễn Lương Bằng, Đống Đa", "Hà Nội"),
        ("TP.HCM : Tầng 6, Quận 7", "TP.HCM"),
        ("Đà Nẵng", "Đà Nẵng"),
        (None, None),
    ],
)
def test_extract_city(location_raw, expected):
    assert extract_city(location_raw) == expected


@pytest.mark.parametrize(
    ("raw_city", "expected"),
    [
        ("TP.HCM", "Hồ Chí Minh"),
        ("tp hcm", "Hồ Chí Minh"),
        ("Thành phố Đà Nẵng", "Đà Nẵng"),
        ("Hà Nội", "Hà Nội"),
        ("  Đà   Nẵng  ", "Đà Nẵng"),
        ("Bình Dương", "Bình Dương"),
        (None, None),
    ],
)
def test_normalize_city(raw_city, expected):
    assert normalize_city(raw_city) == expected


@pytest.mark.parametrize(
    ("location_raw", "expected"),
    [
        ("Hà Nội : 204 Nguyễn Lương Bằng, Đống Đa", "204 Nguyễn Lương Bằng, Đống Đa"),
        ("TP.HCM : Tầng 6, Quận 7", "Tầng 6, Quận 7"),
        ("Đà Nẵng", None),
        ("Hà Nội:", None),
        (None, None),
    ],
)
def test_extract_address(location_raw, expected):
    assert extract_address(location_raw) == expected


@pytest.mark.parametrize(
    ("location_raw", "expected"),
    [
        ("Hà Nội : 204 Nguyễn Lương Bằng, Đống Đa", ("Hà Nội", "204 Nguyễn Lương Bằng, Đống Đa")),
        ("TP.HCM : Tầng 6, Quận 7", ("Hồ Chí Minh", "Tầng 6, Quận 7")),
        ("Đà Nẵng", ("Đà Nẵng", None)),
        (None, (None, None)),
    ],
)
def test_normalize_location(location_raw, expected):
    assert normalize_location(location_raw) == expected


def test_transform_location_is_backward_compatible():
    assert transform_location("TP.HCM : Tầng 6, Quận 7") == (
        "Hồ Chí Minh",
        "Tầng 6, Quận 7",
    )
