def prime(n):
    x = 0
    for i in range(1, n+1):
        if n%i == 0:
            i += 1
    if x == 2:
        print("Prime number")
    else:
        print("Not prime number")
prime(int(input("Enter n:")))
