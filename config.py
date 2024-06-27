import os

class Config:
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
    DYNAMIC_PRICING_BASE = 50  # Base price for parking

