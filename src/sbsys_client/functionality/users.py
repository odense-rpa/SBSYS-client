from sbsys_client.client import SBSYSClient
from sbsys_client.utils import sanitize_cpr

class SBSYSUsers_Client:
    def __init__(self, client: SBSYSClient):
        self.client = client

    def get_user(self, cpr: str) -> dict:
        """
        Fetch user details by CPR number.
        
        :param cpr: The CPR number of the user.
        :return: User details as a dictionary.
        """
        sanitized_cpr = sanitize_cpr(cpr)
        self.client.set_json_body({"CprNummer": sanitized_cpr})
        response = self.client.get("/api/bruger/search")
        return response.json()