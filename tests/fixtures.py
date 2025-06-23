import pytest
import os

from dotenv import load_dotenv
from sbsys_client.functionality.users import SBSYSUsers_Client

@pytest.fixture
def base_client():
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    base_url = os.getenv("BASE_URL")
    token_url = os.getenv("TOKEN_URL")
    instance = os.getenv("INSTANCE")

    if not all([client_id, client_secret, username, password, base_url, token_url, instance]):
        raise ValueError("Missing environment variables for SBSysClient initialization")

    return SBSYSUsers_Client(
        client_id=client_id,
        client_secret=client_secret,
        username=username,
        password=password,
        base_url=base_url,
        token_url=token_url,
        instance=instance
    )

@pytest.fixture
def user_client(base_client):
    return SBSYSUsers_Client(base_client)
        