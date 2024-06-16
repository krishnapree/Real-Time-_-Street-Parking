import os

class Config:
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    TWILIO_ACCOUNT_SID = 'AC723ff75eb26c998305921ba3386d4806'
    TWILIO_AUTH_TOKEN = '8b6001f18e6227baf9449d346a750130'
    TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
