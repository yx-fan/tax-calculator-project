import pytest
import json

def test_calculate_tax_success(client):
    """
    Test successful tax calculation using real 5001 data.
    """
    response = client.post("/calculate-tax", json={"annual_income": 100000, "tax_year": 2022})
    print("DEBUG: response.json =", response.json)

    assert response.status_code == 200
    assert "total_taxes" in response.json
    assert "effective_tax_rate" in response.json
    assert isinstance(response.json["tax_breakdown"], list)

def test_calculate_tax_missing_fields(client):
    """
    Test if missing fields return an error.
    """
    response = client.post("/calculate-tax", json={"annual_income": 100000})
    print("DEBUG: response.json =", response.json)

    assert response.status_code == 400
    assert "error" in response.json


def test_calculate_tax_invalid_year(client):
    """
    Test if an invalid tax year returns an error.
    """
    response = client.post("/calculate-tax", json={"annual_income": 100000, "tax_year": 2018})
    print("DEBUG: response.json =", response.json)

    assert response.status_code == 400
    assert "error" in response.json

def test_calculate_tax_invalid_data(client):
    """
    Test if non-numeric input is handled correctly.
    """
    response = client.post("/calculate-tax", json={"annual_income": "abc", "tax_year": "xyz"})
    print("DEBUG: response.json =", response.json)

    assert response.status_code == 400
    assert "error" in response.json
