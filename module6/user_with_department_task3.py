# import json
# import csv
#
# class DepartmentName(Exception):
#     pass
#
#
# def user_with_department(csv_file, user_json, department_json):
#     with open(user_json, 'r') as f_user:
#         user_data = json.load(f_user)
#         print(user_data)
#     with open(department_json, 'r') as f_depart:
#         depart_data = json.load(f_depart)
#         print(depart_data)
#
#     list_to_csv = [['name', 'department']]
#     for i in user_data:
#         user_name = i['name']
#         # print(user_name)
#         user_dep_id = i['department_id']
#         # print(user_dep_id)
#         # try:
#         for j in depart_data:
#             if j['id'] == user_dep_id:
#                 user_department_name = j['name']
#                 print(user_department_name)
#         list_to_add = [user_name, user_department_name]
#         list_to_csv.append(list_to_add)
#         print(list_to_csv)
#         # except DepartmentName:
#         #     pass
#         with open(csv_file, 'w', newline='') as file:
#             csv_writer = csv.writer(file)
#             csv_writer.writerows(list_to_csv)
#
# user_with_department('jsons_task3/result.csv', 'jsons_task3/user.json', 'jsons_task3/department.json')


import json
import jsonschema
from jsonschema import validate
import csv


class InvalidInstanceError(Exception):
    pass


class DepartmentName(Exception):
    pass


def validate_json(data, schema):
    try:
        jsonschema.validate(data, schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"Validation Error: {e}")
        return False


def user_with_department(csv_file, user_json, department_json):
    # Load JSON data
    with open(user_json, 'r') as file:
        user_data = json.load(file)

    with open(department_json, 'r') as file:
        department_data = json.load(file)

    # Validate JSON data
    user_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "department_id": {"type": "integer"}
        },
        "required": ["id", "name", "department_id"]
    }
}

    department_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"}
        },
        "required": ["id", "name"]
        }
    }

    try:
        jsonschema.validate(instance=user_data, schema=user_schema)
    except:
        raise InvalidInstanceError("Error in user schema")

    try:
        jsonschema.validate(instance=department_data, schema=department_schema)
    except jsonschema.exceptions.ValidationError:
        raise InvalidInstanceError("Error in department schema")

    # Create a mapping of department IDs to department names
    department_mapping = {department['id']: department['name'] for department in department_data}

    # Generate CSV data
    csv_data = []
    for user in user_data:
        department_id = user.get('department_id')
        department_name = department_mapping.get(department_id)
        if department_name is None:
            raise DepartmentName(f"Department with id {department_id} doesn't exists")
        csv_data.append((user['name'], department_name))

    # Write to CSV
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["name", "department"])
        writer.writerows(csv_data)



try:
    user_with_department('jsons_task3/result.csv', 'jsons_task3/user.json', 'jsons_task3/department.json')
except InvalidInstanceError as e:
    print(e)
except DepartmentName as e:
    print(e)