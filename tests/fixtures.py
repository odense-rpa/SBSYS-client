import pytest
import os

from dotenv import load_dotenv

@pytest.fixture
def base_client():
    class BaseClient:
        def __init__(self):
            self.client_id = os.getenv("CLIENT_ID")
            self.client_secret = os.getenv("CLIENT_SECRET")
            self.username = os.getenv("USERNAME")
            self.password = os.getenv("PASSWORD")
            self.base_url = os.getenv("BASE_URL")
            self.token_url = os.getenv("TOKEN_URL")
            self.instance = os.getenv("INSTANCE")

            # Add more environment variables as needed