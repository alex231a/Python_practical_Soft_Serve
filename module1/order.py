def order(a):
    if len(a) <= 1:
        return "Sorted in ascending order"
    ascending = descending = True
    for i in range(1, len(a)):
        if a[i] > a[i - 1]:
            descending = False
        elif a[i] < a[i - 1]:
            ascending = False
    if ascending:
        return "ascending"
    elif descending:
        return "descending"
    else:
        return "not sorted"

    # Example usage:
arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1]
arr3 = [3, 1, 2, 4, 5]

print(order(arr1))  # Output: "Sorted in ascending order"
print(order(arr2))  # Output: "Sorted in descending order"
print(order(arr3))  # Output: "Not sorted"
