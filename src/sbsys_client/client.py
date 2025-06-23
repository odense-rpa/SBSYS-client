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

class SBSYSClient:
    api: dict

    def __init__(self, base_url: str, client_id: str, client_secret: str, username: str, password: str, token_url: str, instance: str):
        
         # Set up logging
        self.logger = logging.getLogger(__name__)

        logging.getLogger("httpx").setLevel(logging.WARNING)
        logging.getLogger("httpcore").setLevel(logging.WARNING)
        
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
        self.client.token = token  # Assign the whole token dict
        return token
    
    def _normalize_url(self, endpoint: str) -> str:
        """Ensure the URL is absolute, handling relative URLs."""
        if endpoint.startswith("http://") or endpoint.startswith("https://"):
            return endpoint
        endpoint = endpoint.lstrip('/')
        return urljoin(self.base_url, endpoint)

    def get(self, endpoint: str, **kwargs) -> httpx.Response:
        """Generic GET request."""
        url = self._normalize_url(endpoint)
        response = self.client.get(url, **kwargs)
        self._handle_errors(response)
        return response

    def post(self, endpoint: str, json: dict, **kwargs) -> httpx.Response:
        """Generic POST request."""
        url = self._normalize_url(endpoint)
        response = self.client.post(url, json=json, **kwargs)
        self._handle_errors(response)
        return response

    def put(self, endpoint: str, json: dict, **kwargs) -> httpx.Response:
        """Generic PUT request."""
        url = self._normalize_url(endpoint)
        response = self.client.put(url, json=json, **kwargs)
        self._handle_errors(response)
        return response

    def delete(self, endpoint: str, **kwargs) -> httpx.Response:
        """Generic DELETE request."""
        url = self._normalize_url(endpoint)
        response = self.client.delete(url, **kwargs)
        self._handle_errors(response)

    def _handle_errors(self, response: httpx.Response):    
        if response.is_error:
            self.logger.error(f"Response: {response.status_code} - {response.text}")
            
        response.raise_for_status()