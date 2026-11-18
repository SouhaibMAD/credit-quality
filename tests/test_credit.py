import pytest
from credit import calculate_risk


def test_high_risk():
    assert calculate_risk(1000, 700) == "HIGH"


def test_medium_risk():
    assert calculate_risk(1000, 400) == "MEDIUM"


def test_low_risk():
    assert calculate_risk(1000, 100) == "LOW"


def test_zero_income():
    assert calculate_risk(0, 100) == -1


def test_negative_income():
    assert calculate_risk(-500, 100) == -1


def test_zero_debt():
    assert calculate_risk(1000, 0) == "LOW"


def test_ratio_exactly_0_3_is_low():
    assert calculate_risk(1000, 300) == "LOW"


def test_ratio_exactly_0_6_is_medium():
    assert calculate_risk(1000, 600) == "MEDIUM"