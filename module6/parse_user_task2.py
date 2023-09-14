import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


def parse_user(output_file, *input_files):
    check_list = []
    output_list = []
    for i in input_files:
        try:
            with open(i, 'r') as json_file:
                data = json.load(json_file)
                for j in data:
                    try:
                        name = j['name']
                        if name not in check_list:
                            check_list.append(name)
                            output_list.append(j)
                            print(check_list)
                            print(output_list)
                    except KeyError as e:
                        pass
        except FileNotFoundError:
            logging.error(f'File {i} doesn\'t exist')

    with open(output_file, 'w') as file:
        json.dump(output_list, file, indent=4)


parse_user("jsons_task2/user4.json", "user_without_name.json")

# parse_user('jsons_task2/result.json', 'jsons_task2/user1.json', 'jsons_task2/user2.json', 'jsons_task2/user5.json')
# parse_user("user4.json", "user_without_name.json")