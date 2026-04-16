'''
Write a Python script to perform below operations on set:
1.
Create two different sets with the data.
2.
Print set items.
3.
Add/remove items in/from a set.
4.
Perform operations on sets: union, intersection, difference, symmetric difference, check subset of another set.
'''

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Set 1:", set1)
print("Set 2:", set2)

set1.add(7)          
set1.remove(2)       

print("\nSet 1 after add/remove:", set1)

print("\nUnion:", set1.union(set2))

print("Intersection:", set1.intersection(set2))

print("Difference (set1 - set2):", set1.difference(set2))

print("Symmetric Difference:", set1.symmetric_difference(set2))

print("Is set1 subset of set2?", set1.issubset(set2))
