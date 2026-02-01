import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "booking_plattform"
DB_USER = "postgres"
DB_PASSWORD = os.getenv("DB_PASSWORD")
