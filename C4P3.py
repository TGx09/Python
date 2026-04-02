lst = []
n = int(input("How many elements? "))

for i in range(n):
    val = int(input("Enter value: "))
    lst.append(val)
print()

def abc(p):
    l1 = []
    for i in p:
        if i not in l1:
            l1.append(i)
    print("l1 = ", l1)
print("lst:", lst)
abc(lst)
