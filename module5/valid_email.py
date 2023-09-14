# Write the function valid_email(...) to check if the input string is a valid email address or not.
#
# An email is a string (a subset of ASCII characters) separated into two parts by @ symbol,
# a “user_info” and a domain_info, that is personal_info@domain_info:
# in case of correct email the function should be displayed the corresponding message – "Email is valid"
# in case of incorrect email the function should be displayed the corresponding message – "Email is not valid"
#
# Note: in the function you must use the "try except" construct.

import re


def valid_email(email):
    try:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z-]+\.[a-zA-Z-.]+$'
        if re.match(pattern, email):
            return "Email is valid"
        else:
            raise ValueError("Email is not valid")
    except ValueError as e:
        return e
