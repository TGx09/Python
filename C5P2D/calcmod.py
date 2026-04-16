def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def sqr(a):
    return a ** 2

def fact(a):
    if a < 0:
        print("Error: Number is negative.")
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result