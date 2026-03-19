def factorial(n):
    f = 1
    for i in range(n , 0, -1):
        f = f * i
    return f
print(factorial(10))