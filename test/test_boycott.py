import pytest
from boycott import check_location, check_product


def test_check_location_found():
    location_name = "Carrefour"
    result = check_location(location_name)
    assert "carrefour" in result["name"].lower()


def test_location_boycotted():
    result = check_location("Carrefour")
    assert result is not None
    assert result["boycotted"] is True


def test_check_product_not_boycotted():
    result = check_product("Hamadi Abid")
    assert result is not None
    assert result["boycotted"] is False


def test_check_location_case_insensitive():
    location_name = "CARREFOUR"
    result = check_location(location_name)
    assert "carrefour" in result["name"].lower()
