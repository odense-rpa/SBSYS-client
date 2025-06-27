from .fixtures import user_client, base_client
from sbsys_client import User_Client


def test_get_user(user_client):
    uuid = "ikke sat"
    user = user_client.get_user(uuid)

    # Assertions to validate the response
    assert isinstance(user, dict), "User details should be a dictionary"
    # Add more specific assertions based on the expected response structure
    # For example:
    # assert "uuid" in user, "User should have a uuid field"
    # assert user["uuid"] == uuid, "Returned user UUID should match requested UUID"


def test_search_users(user_client):
    """Test searching for users with search criteria."""
    search_criteria = {
        "LogonId": "ikke"
    }
    
    users = user_client.search_users(search_criteria)

    # Assertions to validate the response
    assert users[0]["LogonId"] == "ikke"

