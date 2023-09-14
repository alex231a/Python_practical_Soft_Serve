def studying_hours(a):
    max_length = 1  # Initialize the maximum length to 1
    current_length = 1  # Initialize the current length to 1

    for i in range(1, len(a)):
        if a[i] >= a[i - 1]:
            current_length += 1
        else:
            current_length = 1

        if current_length > max_length:
            max_length = current_length

    return max_length


# Example usage:
a = [2, 2, 1, 3, 4, 1]
result = studying_hours(a)
print(result)  # Output: 3