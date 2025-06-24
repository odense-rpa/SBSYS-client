from .fixtures import base_client, user_client
from sbsys_client.functionality.user_client import User_Client


def test_get_user(user_client):
    cpr = "222222-2222"  # Example CPR number, replace with a valid one for your tests
    user_details = user_client.get_user(cpr)

    # Assertions to validate the response
    assert isinstance(user_details, list), "User details should be a list"
    assert len(user_details) == 1, "User details list should contain exactly one entry"
    user_details = user_details[0]
    assert user_details["CprNummer"] == cpr