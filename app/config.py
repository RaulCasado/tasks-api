import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    HOSTNAME = os.getenv('HOSTNAME')
    DATABASE = os.getenv('DATABASE')
    PORT = os.getenv('PORT')
    DB_USERNAME = os.getenv('DB_USERNAME')
    PASSWORD = os.getenv('PASSWORD')
    
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
