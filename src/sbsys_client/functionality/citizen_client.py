from sbsys_client.client import SBSYSClient
from sbsys_client.utils import sanitize_cpr

class Citizen_Client:
    def __init__(self, client: SBSYSClient):
        self.client = client

    def get_citizen(self, cpr: str) -> dict:
        """
        Fetch citizen details by CPR number.
        
        :param cpr: The CPR number of the citizen.
        :return: Citizen details as a dictionary.
        """
        cpr = sanitize_cpr(cpr)
        response = self.client.post("/api/person/search", json={"CprNummer": cpr})
        return response.json()
