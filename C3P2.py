'''
Write a python program to read n numbers from a user and print:
Number of positive numbers.
Number of negative numbers.
Number of zeros.
Number of odd numbers.
Number of even numbers.
Average of all numbers.
'''
pc = 0
nc = 0
zc = 0
oc = 0
ec = 0

n = int(input("Enter number of elements:\t"))

number = []

for i in range(1, n + 1):
    num = int(input(f"Enter element {i}:\t"))
    number.append(num)
print()

for i in number:
    if i > 0:
        pc += 1
    elif i < 0:
        nc += 1
    else:
        zc += 1

for i in number:
    if i % 2 == 0:
        ec += 1
    else:
        oc += 1

avg = sum(number)/len(number)
print()

print("All numbers:\t", number)
print("No. of Positive numbers:\t", pc)
print("No. of Negative numbers:\t", nc)
print("No. of Zeros:\t", zc)
print("No. of Odd numbers:\t", oc)
print("No. of even numbers:\t", ec)
if avg <= 0:
    print("Average cant be calcuated with negative numbers.")
else:
    print("Average:\t", avg)
