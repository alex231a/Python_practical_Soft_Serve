def findPermutation(p, q):
    n = len(p)
    p_dict = {p[i]: i for i in range(n)}
    r = [0] * n
    for i in range(n):
        r[i] = p_dict[q[i]] + 1
    return r


# Example usage:
p = [5, 1, 3]
q = [3, 1, 5]
r = findPermutation(p, q)
print(r)  # Output: [3, 2, 1]
