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

y = input("Enter any letter to count: ")
print("count:", r.count(f"{y}"))
print()

w = input("Check start with: ")
print("starts with:", r.startswith(f"{w}"))
print()

v = input("Check End with: ")
print("End with:", r.endswith(f"{v}"))
print()

u = input("Split at: ")
print("split:", r.split(f"{u}"))