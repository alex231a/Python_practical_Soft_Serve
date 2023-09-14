def isPalindrome(str):
    count = 0
    if len(str) < 1:
        raise Exception("The length of input string should be at least 1 letters) ")
    my_dict = {}
    for i in str:
        if my_dict.get(i) != None:
            my_dict[i] = my_dict[i] + 1
        else:
            my_dict[i] = 1
    for v in my_dict.values():
        if v % 2 != 0:
            count += 1
    if count <= 1:
        return True
    else:
        return False

print(isPalindrome('abb'))

