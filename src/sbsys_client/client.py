import httpx
import json
import logging
from authlib.integrations.httpx_client import OAuth2Client
from urllib.parse import urljoin

def _format_json(data: dict) -> str:
    """Format JSON data for logging.
    :param data: The JSON data to format.
    :return: A formatted string representation of the JSON data.
    """
    return json.dumps(data, indent=2)

class SBSysClient:
    api: dict

    def __init__(self, base_url: str, client_id: str, client_secret: str, username: str, password: str, token_url: str, instance: str):
        self.base_url = base_url
        self.client = OAuth2Client(
            client_id=client_id,
            client_secret=client_secret,
        )
        self.username = username
        self.password = password
        self.token_url = token_url  # Save token_url for later use
        self.client.token = self.fetch_token()

    def fetch_token(self):
        """Fetch OAuth2 token using password grant type."""
        data = {
            "grant_type": "password",
            "client_id": self.client.client_id,
            "client_secret": self.client.client_secret,
            "username": self.username,
            "password": self.password,
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = httpx.post(self.token_url, data=data, headers=headers)
        response.raise_for_status()
        token = response.json()
        self.client.token = token
        return token["access_token"]


