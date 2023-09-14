import json


def find(file, key):
    unique_values = set()  # To store unique values of the key

    def search_for_key(data):
        if isinstance(data, dict):
            for k, v in data.items():
                if k == key:
                    if isinstance(v, list):
                        unique_values.update(v)
                    else:
                        unique_values.add(v)
                elif isinstance(v, (dict, list)):
                    search_for_key(v)
        elif isinstance(data, list):
            for item in data:
                search_for_key(item)

    try:
        with open(file, 'r') as json_file:
            data = json.load(json_file)
            search_for_key(data)

    except (FileNotFoundError, json.JSONDecodeError):
        pass  # Handle file not found or invalid JSON gracefully

    return list(unique_values)

# Test cases
result1 = find("jsons_task1/1.json", "password")
result2 = find("jsons_task1/2.json", "password")
result3 = find("jsons_task1/3.json", "password")

print(result1)  # Should print ["pass_1", "qwerty"]
print(result2)  # Should print ["1234qweQWE", "pass_1", "qwerty"]
print(result3)  # Should print ["1234qweQWE"]