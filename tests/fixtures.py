import pytest
import os

from dotenv import load_dotenv
from sbsys_client import SBSYSClient, Citizen_Client, Cases_Client, User_Client

load_dotenv()

@pytest.fixture
def base_client():
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    base_url = os.getenv("BASE_URL")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    token_url = os.getenv("TOKEN_URL", "default_token_url")
    instance = os.getenv("INSTANCE", "default_instance")

    if not all([client_id, client_secret, base_url, username, password, token_url, instance]):
        raise ValueError("Missing environment variables for Client initialization")

    return SBSYSClient(
        client_id=client_id,
        client_secret=client_secret,
        base_url=base_url,
        username=username, 
        password=password,
        token_url=token_url,
        instance=instance
    )

@pytest.fixture
def citizen_client(base_client):
    return Citizen_Client(base_client)

@pytest.fixture
def cases_client(base_client):
    return Cases_Client(base_client)

@pytest.fixture
def user_client(base_client):
    return User_Client(base_client)
