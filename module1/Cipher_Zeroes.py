def Cipher_Zeroes(N):
    # if int(N) <= 1:
    #     raise Exception("Wrong input value.")
    zero_count = 0
    for digit in N:
        if digit in "069":
            zero_count += 1
        elif digit == "8":
            zero_count += 2

    if zero_count % 2 == 0 and zero_count > 0:
        points = zero_count #// 2
        points -= 1  # Deduct one point as per the rule
    else:
        points = (zero_count + 1) #// 2  # Add one point as per the rule

    binary_result = bin(points)[2:]  # Convert to binary without "0b" prefix

    if zero_count == 0:
        result = 0
        return result
    else:
        return binary_result  # Return binary as a string

# Example usage:
N = "4"
result = Cipher_Zeroes(N)
print(result)  # Output: "10"