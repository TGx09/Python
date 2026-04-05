lst = []

for i in range(int(input("How many elements? "))):
    lst.append(int(input("Enter value: ")))
print()

def abc(p):
    l1 = []
    for i in p:
        if i not in l1:
            l1.append(i)
    print("l1 = ", l1)
print("lst:", lst)
abc(lst)
