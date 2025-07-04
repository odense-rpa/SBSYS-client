from sbsys_client.client import SBSYSClient
from sbsys_client.utils import sanitize_cpr

class User_Client:
    def __init__(self, client: SBSYSClient):
        self.client = client

    def get_user(self, uuid: str) -> dict:
        """
        Fetch citizen details by CPR number.
        
        :param cpr: The CPR number of the citizen.
        :return: Citizen details as a dictionary.
        """
        response = self.client.get(f"/api/bruger/{uuid}")
        return response.json()
    
    def search_users(self, search_criteria: dict) -> dict:

        reponse = self.client.post("/api/bruger/search", json=search_criteria)
        return reponse.json()