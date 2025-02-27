import pytest
from app.services.tax_calculation_service import calculate_taxes

def test_calculate_taxes_valid():
    """
    Test calculate_taxes() with valid inputs.
    """
    result = calculate_taxes(160000, 2022)
    print("DEBUG: calculate_taxes(160000, 2022) =", result)

    assert result["annual_income"] == 160000
    assert result["total_taxes"] == 33448.85
    assert result["effective_tax_rate"] == 20.91
    assert isinstance(result["tax_breakdown"], list)
    assert len(result["tax_breakdown"]) == 5
    assert result["tax_breakdown"][0]["tax_amount"] == 7529.55
    assert result["tax_breakdown"][1]["tax_amount"] == 10289.97
    assert result["tax_breakdown"][2]["tax_amount"] == 14360.58
    assert result["tax_breakdown"][3]["tax_amount"] == 1268.75
    assert result["tax_breakdown"][4]["tax_amount"] == 0

def test_calculate_taxes_invalid_year():
    """
    Test calculate_taxes() when tax year is not found.
    """
    result = calculate_taxes(100000, 2018)
    print("DEBUG: calculate_taxes(100000, 2018) =", result)

    assert "error" in result
    assert result["error"] == "Tax brackets for 2018 not found in cache"
