import re
from functools import reduce


def create_account(user_name, password, secret_words):
    password_pattern = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*_])[A-Za-z0-9!@#$%^&*_]{6,}$")

    def has_one_misspelled_word(actual, provided):
        print(actual)
        print(provided)
        dict_check = {}
        if len(actual) == len(provided):
            res = True
            dict_check['len'] = res
        else:
            res = False
            dict_check['len'] = res

        if dict_check['len']:
##################################Filter Lambla####################################################
            # actual.sort()
            # provided.sort()
            # print(actual)
            # print(provided)

            # res = list(filter(lambda i: i in provided, actual))
            # print(res)
            # differences = len(actual) - len(res)
            # print(differences)
##################################Set####################################################
            # s_actual = set(actual)
            # s_provided = set(provided)
            # print(s_actual)
            # print(s_provided)
            # res = s_actual - s_provided
            # print('result set - set')
            # print(res)
            # differences = len(res)
            # print(differences)
############################LOOP###########################################################
            res = []
            for x in actual:
                if x in provided:
                    provided.remove(x)
                    res.append(x)
            print(res)
            differences = len(actual) - len(res)





############################################################################################
            if differences > 1:
                res = False
            else:
                res = True
            dict_check['misspelled '] = res

        if all(dict_check.values()):
            return True
        else:
            return False

    # Check if the password meets the requirements.
    if not password_pattern.match(password):
        raise ValueError("Password must contain at least 6 symbols, including one uppercase letter, one lowercase letter, one special character, and one number.")

    # Function to check the credentials.
    def check(input_password, input_secret_words):
        if input_password == password and has_one_misspelled_word(secret_words, input_secret_words):
            return True
        return False

    return check


# user2 = create_account("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
# print(user2("yu6r*Tt5",["abc3", "word1", "zzzzzz"]))


# # list_a = [8, 2, 9, 4, 7, 11, 99, 99]
# # list_b = [5, 2, 3, 4, 1, 33, 33, 33]
# list_a = ["word1", "abc3", "list"]
# list_b = ["abc3", "word1", "zzzzzz"]

# list_a = ['1', '1', '2']
# list_b = ['1', '1', '4']

list_a = ['1', '1', '2']
list_b = ['1', '3', '4']

user3 = create_account("User2", "yu6r*Tt5", list_a)
print(user3("yu6r*Tt5",list_b))

# res = []
# for x in list_a:
#     if x in list_b:
#         list_b.remove(x)
#         res.append(x)
# print(res)
# len_res = len(res)
