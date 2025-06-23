import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
base_url = os.getenv("BASE_URL")
token_url = os.getenv("TOKEN_URL")
instance = os.getenv("INSTANCE")