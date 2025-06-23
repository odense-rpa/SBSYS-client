import os
import logging
from dotenv import load_dotenv

from sbsys_client.client import SBSysClient


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


client = SBSysClient(
    base_url=base_url,
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    token_url=token_url,
    instance=instance
)
