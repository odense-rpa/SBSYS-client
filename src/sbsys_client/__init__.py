from .client import SBSYSClient
from .functionality import Citizen_Client, Cases_Client, User_Client

def hello() -> str:
    return "Hello from sbsys-client!"

__all__ = ["SBSYSClient", "Citizen_Client", "Cases_Client", "User_Client", "hello"]
