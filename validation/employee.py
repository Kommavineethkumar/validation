import re

"""
This function validates the name and places the following constraints on the name
* The name cannot start with a space
* The name should have atleast 5 characters
* The name can have maximum of 30 characters
"""
def validateName(name):
    if not re.match("^[a-zA-Z][a-zA-Z ]{4,29}$", name):
        return False
    return True

"""
This function validates whether passed paramater is a number or not
"""
def validateNumber(number):
    if not re.match("^[0-9 -]+$", number):
        return False
    return True

"""
This function validates whether passed parameter is an valid email or not
"""
def validateEmailAddress(email):
    if not re.match(r"^\S+@\S+\.\S+$", email):
        return False
    return True

"""
It accepts the dates with the following formats:
DD/MM/YYYY
DD-MM-YYYY
"""
def validateDate(date):
    if re.match("^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$", date) or re.match("^[0-9]{1,2}\\-[0-9]{1,2}\\-[0-9]{4}$", date):
        return True
    return False

"""
This function validates whether passed parameter is a valid mobile number or not
"""
def validateMobileNumber(mobileNumber):
    if not re.match("^[0-9]{10}$", mobileNumber):
        return False
    return True

"""
This function validates whether passed parameter is a valid address or not
"""
def validateAddress(address):
    if not re.match("^[0-9]{0,5}[a-zA-Z0-9- ]*", address):
        return False
    return True
