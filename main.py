import os
import logging
from dotenv import load_dotenv

from sbsys_client.client import SBSYSClient
from sbsys_client.functionality.user_client import User_Client


# Load environment variables from .env file
load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
base_url = os.getenv("BASE_URL")
token_url = os.getenv("TOKEN_URL")
instance = os.getenv("INSTANCE")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


client = SBSYSClient(
    base_url=base_url,
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    token_url=token_url,
    instance=instance
)

# Create an instance of Users_Client and pass the SBSYSClient instance
users_client = User_Client(client)

# Call the get_user method on the instance
user_details = users_client.get_user(cpr="222222-2222")  # Example CPR number, replace with a valid one for your tests
print(user_details)
