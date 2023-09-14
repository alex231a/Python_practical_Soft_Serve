import re


def pretty_message(data):
    data_input = data.split(' ')
    pattern = r"^[0]?[a-z]*[a-z]{4}[7]*"
    result_list = []
    for i in data_input:
        res = re.findall(pattern, i)
        if res != []:
            if res[0] == '0bbcd7':
                res[0] = ' 0bbcd7'
            result_list.append(res[0])
    result_str = ' '.join(result_list)
    return result_str






data = "0msdfgh 00000xbcd 0bbcd7 hjkj00wjhg hjkj0ajhg"
print(pretty_message(data))

# 0msdfgh 00000xbcd 0bbcd7 hjkj00wjhg hjkj0ajhg
# 0msdfgh 0bbcd7 hjkj hjkj
# 0msdfgh 0bbcd7 hjkj hjkj
