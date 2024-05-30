# test_config.py
import os

class Config:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SECRET_KEY = 'test_secret_key'
    WTF_CSRF_ENABLED = False  # Disable CSRF for testing
