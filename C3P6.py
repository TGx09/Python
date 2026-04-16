'''
Write a Python script to perform below operations on dictionary:
1.
Create a dictionary.
2.
Print dictionary items.
3.
Add/remove key-value pair in/from a dictionary.
4.
Check whether a key exists in a dictionary.
5.
Iterate through a dictionary.
6.
Concatenate multiple dictionaries.
'''

dict1 = {"name": "John", "age": 20, "city": "New York"}

print("Original Dictionary:", dict1)

dict1["course"] = "Python"

dict1.pop("age")

print("\nDictionary after add/remove:", dict1)

key = "name"
if key in dict1:
    print("\nKey exists")
else:
    print("\nKey does not exist")

print("\nIterating through dictionary:")
for k, v in dict1.items():
    print(k, ":", v)

dict2 = {"country": "USA", "status": "Student"}

dict3 = dict1.copy()
dict3.update(dict2)

print("\nConcatenated Dictionary:", dict3)
