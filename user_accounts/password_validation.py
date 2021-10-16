import re


def password_checking(args):
    # Checking weather string is greater or equal than 8
    character_count_check = False
    if len(args) >= 8:
        character_count_check = True
    # Checking first letter is numeric or not
    number_check = args[0].isdigit()
    # Checking Is there any uppercase character in password
    uppercase_check = any(ele.isupper() for ele in args)
    # Checking Is there any lowercase character in password
    lower_check = any(ele.islower() for ele in args)

    # For checking special character, we have to use regex operation
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    # Pass the string in search
    # method of regex object.
    special_character_check = False
    if regex.search(args) is not None:
        special_character_check = True

    error_response = {}

    # return value
    if number_check:
        temp = {"number_check": "First Letter can't be a number."}
        error_response.update(temp)
    if not uppercase_check:
        temp = {"uppercase_check": "Password must contain a Uppercase character."}
        error_response.update(temp)
    if not lower_check:
        temp = {"lower_check": "Password must contain a Lowercase character"}
        error_response.update(temp)
    if not special_character_check:
        temp = {"special_character_check": "Password must contain a special character"}
        error_response.update(temp)
    if not character_count_check:
        temp = {"character_count_check": "Password must be consist of 8 or more characters"}
        error_response.update(temp)

    return error_response
