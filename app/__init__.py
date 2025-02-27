import sys
import logging
from flask import Flask
from flask_cors import CORS
from config import CurrentConfig
from app.routes import tax_bp
from app.services.redis_service import create_redis_client
from app.services.cache_data_service import cache_all_tax_brackets
from app.utils import log_debug, log_info, log_warning, log_error

LOG_LEVEL = logging.DEBUG if CurrentConfig.DEBUG else logging.INFO

def create_app():
    """Flask Application Factory"""
    app = Flask(__name__)
    app.config.from_object(CurrentConfig)

    # Enable CORS for all routes
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Set the logging level for the Flask app and Werkzeug
    app.logger.setLevel(LOG_LEVEL)
    logging.getLogger("werkzeug").setLevel(LOG_LEVEL)
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    # Create a Redis client instance
    redis_client = create_redis_client()

    # Cache all tax brackets when the application starts
    try:
        cache_all_tax_brackets()
    except Exception as e:
        log_error(f"Failed to cache tax brackets: {e}")
        sys.exit(1)

    # Register the tax_bp Blueprint
    app.register_blueprint(tax_bp)

    log_info("Flask application initialized successfully!")
    return app, redis_client
