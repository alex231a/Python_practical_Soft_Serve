def divisor(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i
    while True:
        yield None



two = divisor(2)
print(next(two))
print(next(two))
print(next(two))
print(next(two))



