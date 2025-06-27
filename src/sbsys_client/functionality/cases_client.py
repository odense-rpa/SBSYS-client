from sbsys_client.client import SBSYSClient
from sbsys_client.utils import sanitize_cpr

class Cases_Client:
    def __init__(self, client: SBSYSClient):
        self.client = client

    def get_case(self, case_id: int) -> dict:
        """
        Fetch case details by case ID.
        
        :param case_id: The ID of the case.
        :return: Case details as a dictionary.
        """
        response = self.client.get(f"/api/sag/{case_id}")
        return response.json()

    def get_cases_by_citizen(self, cpr: str) -> dict:
        """
        Fetch all cases for a specific citizen by CPR number.
        
        :param cpr: The CPR number of the citizen.
        :return: List of cases as a dictionary.
        """
        cpr = sanitize_cpr(cpr)
        json = {
            "PrimaerPerson": {
                "CprNummer": cpr
            },
            "Limit": 2000
        }
        response = self.client.post("/api/sag/search", json)
        return response.json()
    
    def get_cases_by_caseid(self, caseid: int) -> dict:
        """
        Fetch cases by case ID with additional search parameters.
        
        :param caseid: The case ID to search for.
        :return: Cases as a dictionary.
        """
        json = {
            "SagsSkabeloner": [
                caseid
            ],
        }
        
        response = self.client.post("/api/sag/search?InkluderParterIResultat=true", json)
        return response.json()

    def create_case(self, case_data: dict) -> dict:
        """
        Create a new case.
        
        :param case_data: Dictionary containing case information.
        :return: Created case details as a dictionary.
        """
        response = self.client.post("/api/case", json=case_data)
        return response.json()

    def update_case(self, case_id: str, case_data: dict) -> dict:
        """
        Update an existing case.
        
        :param case_id: The ID of the case to update.
        :param case_data: Dictionary containing updated case information.
        :return: Updated case details as a dictionary.
        """
        response = self.client.put(f"/api/case/{case_id}", json=case_data)
        return response.json()

    def delete_case(self, case_id: str) -> dict:
        """
        Delete a case by case ID.
        
        :param case_id: The ID of the case to delete.
        :return: Response confirmation as a dictionary.
        """
        response = self.client.delete(f"/api/case/{case_id}")
        return response.json()

    def search_cases(self, search_criteria: dict) -> dict:
        """
        Search for cases based on various criteria.
        
        :param search_criteria: Dictionary containing search parameters.
        :return: Search results as a dictionary.
        """
        response = self.client.post("/api/case/search", json=search_criteria)
        return response.json()