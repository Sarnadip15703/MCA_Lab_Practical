s = input("Enter a string: ")

result = ""

for ch in s:
    if ch == ",":
        result += "."
    elif ch == ".":
        result += ","
    else:
        result += ch

print("Swapped string:", result)
