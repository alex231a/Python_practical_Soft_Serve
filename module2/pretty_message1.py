import re


def pretty_message(data):
    pattern = r'([^,]+:\s[^,]+,\s\d{4})'
    output = re.findall(pattern, data)
    return output



data = "Head First. Python: PROSystem, 2021 and Coding for Kids Python & Blockchain Programming: Elliot Davis, 2022"
print(pretty_message(data))


