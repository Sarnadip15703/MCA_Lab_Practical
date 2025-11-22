s = input("Enter a string: ")

count = 0

for ch in s:
    if ch.isdigit():
        count += 1

print("Total numbers in string:", count)
