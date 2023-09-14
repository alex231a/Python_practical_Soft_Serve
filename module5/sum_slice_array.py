# Write the function sum_slice_array(arr, first, second), which accepts the array (list) arr and two numbers (first and second) -
# the ordinal numbers of the elements of the array that must be added.
# For example, if 3 and 5 were entered, the 3rd and 5th elements must be added.
#
# The function should generate exceptions MyExceptions:
# if non-numbers or numbers less than 1 were entered;
# if non-numbers obtained from array;
# if when one of the numbers or both is larger than the array length.


class MyExceptions(Exception):
    pass


def sum_slice_array(arr, first, second):
    try:
        flag1 = False
        if (isinstance(first, int)) and (isinstance(second, int)):
            flag1 = True
        if flag1 and first >= 1 and second >= 1:
            flag1 = True
        else:
            flag1 = False

        flag2 = False
        if all(isinstance(item, int) for item in arr):
            flag2 = True

        flag3 = False
        if len(arr) > first-1 and len(arr) > second-1:
            flag3 = True
        res_list = [flag1, flag2, flag3]
        if not all(res_list):
            raise MyExceptions('MyExceptions')
    except MyExceptions as e:
        return e
    else:
        num1 = arr[first - 1]
        num2 = arr[second - 1]
        res = float(num1 + num2)
        return res


# my_arr = [1, 2, 3]
# f = -1
# s = 2
#
# print(sum_slice_array(my_arr, f, s))
try:
    print(sum_slice_array([7, 9, 3, 6, 7], 5, 2))
except MyExceptions:
    print("MyExceptions")