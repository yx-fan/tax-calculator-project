import os

class Config:
    """
    General configuration parent class
    """
    DEBUG = False
    TESTING = False
    PORT = os.getenv("PORT", 5002)
    MAX_RETRIES = 10
    REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT = os.getenv("REDIS_PORT", 6379)
    REDIS_DB = os.getenv("REDIS_DB", 0)
    TAX_API_BASE_URL = os.getenv("TAX_API_BASE_URL", "http://localhost:5001/tax-calculator/tax-year/")

class DevelopmentConfig(Config):
    """
    Development configuration child class
    """
    DEBUG = True

class TestingConfig(Config):
    """
    Testing configuration child class
    """
    TESTING = True
    DEBUG = True

class ProductionConfig(Config):
    """
    Production configuration child class
    """
    DEBUG = False
    PORT = os.getenv("PORT", 8000)

    
config_name = os.getenv("FLASK_ENV", "development")
config_dict = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}

CurrentConfig = config_dict.get(config_name)