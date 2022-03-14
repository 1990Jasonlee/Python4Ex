def fibonacci(n):
    x1 = 0
    x2 = 1
    if n <= 2:
        return n
    else:
        for i in range(1, n + 1):
            n = x1 + x2
            x2 = x1
            x1 = n
    return n


print(fibonacci(0))
print(fibonacci(4))
print(fibonacci(5))
