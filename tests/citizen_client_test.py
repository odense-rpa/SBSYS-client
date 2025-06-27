from .fixtures import base_client, citizen_client
from sbsys_client.functionality.citizen_client import Citizen_Client


def test_get_citizen(citizen_client):
    cpr = "2222222222"  # Example CPR number, replace with a valid one for your tests
    citizen = citizen_client.get_citizen(cpr)

    # Assertions to validate the response
    assert isinstance(citizen, list), "Citizen details should be a list"
    assert len(citizen) == 1, "Citizen details list should contain exactly one entry"
    citizen = citizen[0]
    assert citizen["CprNummer"] == "222222-2222"