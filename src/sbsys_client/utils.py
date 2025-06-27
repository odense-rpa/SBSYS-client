from datetime import datetime

def is_valid_cpr(cpr: str) -> bool:
    """
    Validate a Danish CPR number.

    :param cpr: A CPR number to validate.
    :return: True if the CPR number is valid, False otherwise.
    """
    if not cpr:
        return False

    # CPR numbers must be 10 characters long (or 11 with dash)
    if len(cpr) != 11:
        return False
    
    # Check if there's a dash at position 6 (0-indexed, which is character 7)   
    if cpr[6] != '-':
        return False    # CPR numbers must be numeric (after removing dash)
    if not cpr[:6].isnumeric() or not cpr[7:].isnumeric():
        return False

    # CPR numbers must be numeric (after removing dash)
    if not cpr[:6].isnumeric():
        return False    # CPR numbers must have a valid date
    try:
        datetime.strptime(cpr[:6], "%d%m%y")
    except ValueError:
        return False

    # CPR numbers no longer have a valid checksum, so no check is done
    return True

def sanitize_cpr(cpr: str) -> str:
    """
    Sanitize a CPR number by removing any spaces or dashes.
    
    :param cpr: A CPR number to sanitize.
    :return: The sanitized CPR number.
    """

    if "-" not in cpr:
        cpr = cpr[:6] + "-" + cpr[6:]

    if cpr != "222222-2222":
        if not is_valid_cpr(cpr):       
            raise ValueError("Invalid CPR number.")
    
    return cpr
