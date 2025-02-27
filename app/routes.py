from flask import Blueprint, request, jsonify
from app.services.tax_calculation_service import calculate_taxes
from app.utils import log_info, log_error

# Define a Blueprint for the tax routes
tax_bp = Blueprint("tax", __name__)

@tax_bp.route("/", methods=["GET"])
def health_check():
    """
    Health check endpoint for the tax service.
    """
    log_info("Health check endpoint hit.")
    return jsonify({"message": "Tax calculation service is running."})

@tax_bp.route("/calculate-tax", methods=["POST"])
def calculate_tax():
    """
    Calculate taxes based on the provided annual income and tax year.
    """
    try:
        # Parse request JSON
        data = request.get_json()
        if not data:
            log_error("Invalid JSON data received.")
            return jsonify({"error": "Invalid request. Please send JSON data."}), 400

        # Extract required fields
        annual_income = data.get("annual_income")
        tax_year = data.get("tax_year")

        # Validate input types
        if annual_income is None or tax_year is None:
            log_error("Missing required fields: 'annual_income' or 'tax_year'.")
            return jsonify({"error": "Missing required fields: 'annual_income' and 'tax_year'."}), 400

        try:
            annual_income = int(annual_income)
            tax_year = int(tax_year)
        except ValueError:
            log_error("Invalid data types for 'annual_income' or 'tax_year'. Must be integers.")
            return jsonify({"error": "Invalid data types. 'annual_income' and 'tax_year' must be numbers."}), 400

        # Call the tax calculation service
        result = calculate_taxes(annual_income, tax_year)
        print("DEBUG: calculate_taxes() returned:", result)

        # If `calculate_taxes()` returns an error, handle it
        if "error" in result:
            log_error(f"Tax calculation error: {result['error']}")
            return jsonify("Server error. Please try again later."), 500

        # Return successful response
        return jsonify(result), 200

    except Exception as e:
        log_error(f"Unexpected server error: {str(e)}")
        return jsonify({"error": "Internal server error. Please try again later."}), 500
