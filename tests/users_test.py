import pytest

from .fixtures import base_client, user_client

from sbsys_client.functionality.users import SBSYSUsers_Client

def test_get_user(user_client):
    cpr = "1234567890"  # Example CPR number, replace with a valid one for your tests
    user_details = user_client.get_user(cpr)
    
    assert isinstance(user_details, dict), "User details should be a dictionary"
    assert "CprNummer" in user_details, "User details should contain 'CprNummer'"
    assert user_details["CprNummer"] == cpr, f"Expected CPR number {cpr}, got {user_details['CprNummer']}"