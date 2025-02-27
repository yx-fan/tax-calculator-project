import json
from app.services.redis_service import get_redis_client
from app.utils import log_info, log_error

def calculate_taxes(annual_income, tax_year):
    """
    Calculates the total tax, effective tax rate, and breakdown based on tax brackets.

    Args:
        annual_income (float): The user's annual income.
        tax_year (int): The selected tax year.

    Returns:
        dict: A dictionary containing total tax, effective tax rate, and tax breakdown.
    """
    
    redis_client = get_redis_client()
    cache_key = f"tax_brackets:{tax_year}"
    tax_data = redis_client.get(cache_key)

    # Handle missing tax bracket data
    if not tax_data:
        log_error(f"Tax brackets for {tax_year} not found in cache")
        return {"error": f"Tax brackets for {tax_year} not found in cache"}
    
    tax_brackets = json.loads(tax_data).get("tax_brackets", [])

    total_tax = 0
    remaining_income = annual_income
    tax_breakdown = []

    # Iterate through each tax bracket
    for bracket in tax_brackets:
        min_income = bracket["min"]
        rate = bracket["rate"]
        max_income = bracket.get("max")  # Some brackets don't have a max (∞)

        # If no remaining income, ensure tax breakdown consistency
        if remaining_income <= 0:
            tax_breakdown.append({
                "bracket": f"{min_income} - {max_income if max_income else '∞'}",
                "tax_amount": 0
            })
            continue

        # Calculate taxable income in the current bracket
        taxable_income = min(remaining_income, max_income - min_income) if max_income else remaining_income
        tax_amount = taxable_income * rate
        total_tax += tax_amount

        # Store tax breakdown details
        tax_breakdown.append({
            "bracket": f"{min_income} - {max_income if max_income else '∞'}",
            "tax_amount": round(tax_amount, 2)
        })

        # Reduce remaining income for next bracket
        remaining_income -= taxable_income

    # Calculate effective tax rate
    effective_tax_rate = round((total_tax / annual_income) * 100, 2) if annual_income else 0

    log_info(f"Calculated taxes for {annual_income}: Total - {total_tax:.2f}, Effective Rate - {effective_tax_rate:.2f}%")

    return {
        "annual_income": annual_income,
        "total_taxes": round(total_tax, 2),
        "effective_tax_rate": effective_tax_rate,
        "tax_breakdown": tax_breakdown
    }
