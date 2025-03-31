import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///inventory.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email configuration for notifications
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')

    # Barcode Scanner API Key
    BARCODE_API_KEY = os.getenv('BARCODE_API_KEY')
