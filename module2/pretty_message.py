import re


def pretty_message(input_string):
    pattern = r'(\w+)(\1)+'
    input_list = input_string.split(' ')
    output_list = []
    for i in input_list:
        res_search = re.findall(pattern, i)
        while True:
            result = re.sub(pattern, r'\1', i)
            i = result
            res_search = re.findall(pattern, i)
            if res_search == []:
                output_list.append(result)
                break
    output_string = ' '.join(output_list)
    return output_string


# Example usage:
input_string = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
result = pretty_message(input_string)
print(result)