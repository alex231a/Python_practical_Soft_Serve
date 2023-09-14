# from functools import reduce
#
# def compare_lists(list1, list2):
#     # Use reduce to iterate through elements and compare
#     differences = reduce(lambda acc, pair: acc + 1 if pair[0] != pair[1] else acc, zip(list1, list2), 0)
#     return differences
#
# # Example usage
# list_a = [8, 2, 9, 4, 7, 11, 99, 99]
# list_b = [5, 2, 3, 4, 1, 33]
#
# # differences = compare_lists(list_a, list_b)
# # print("Number of differences:", differences)  # Number of differences: 1
# #
# # for i in list_a:
# #     if i in list_b:
# #         print(i)
#
# res = list(filter(lambda i: i not in list_a, list_b))
# print(len(res))
# print(res)
#
#
# a = set(list_a)
# b = set(list_b)
# print(a)
# print(b)
#
# print(a-b)




list_a = ['1', '1', '2']
list_b = ['1', '3', '4']



result=list(set(list_a) & set(list_b))
print(result)
diff = len(list_a) - len(result)
print(diff)