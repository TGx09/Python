f = open("file.txt", "r")
print(f.read())
f.close()

f = open("file.txt", "r") 
print(f.readline())
print(f.readline())
f.close()

f = open("file.txt", "w")
f.write("TG")
f.close()

f = open("file.txt", "r")
print(f.read())

lis = ["Yo!\n", "TG.exe\n", "Iris\n"]
with open("file.txt", "w") as file:
    file.writelines(lis)
    
with open("file.txt", "r") as file:
    print(file.read())