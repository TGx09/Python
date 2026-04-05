s = input("Enter any string: ")
print("s:", s)
print()

print("lowercase: ", s.lower())
print()

print("uppercase: ", s.upper())
print()

r = input("Enter another string: ")
print("Replace string:", s.replace(s, f"{r}" ))
print()

z = input("Enter any string to find: ")
print(f"find {z}:", r.find(f"{z}"))
print()

print("count:", r.count(input("Enter any letter to count: ")))
print()

print("starts with:", r.startswith(input("Check start with: ")))
print()

print("End with:", r.endswith(input("Check End with: ")))
print()

print("split:", r.split(input("Split at: ")))
