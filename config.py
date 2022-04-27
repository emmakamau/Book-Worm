## Configuration files 
import os

class Config:
    BOOKS_API_BASE_URL = 'https://www.googleapis.com/books/v1/volumes?q={}?api_key={}'
    BOOKS_API_KEY = os.environ.get('BOOKS_API_KEY')
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    pass

class ProdConfig(Config):
    # (Production  configuration child class
    # Args:Config: The parent configuration class with General configuration settings)

    pass

class DevConfig(Config):
    # (Development configuration child class
    # Args:Config: The parent configuration class with General configuration settings)
    
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
