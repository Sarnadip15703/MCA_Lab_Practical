len=input("Enter the string")

count = 0
for ch in len:
    if ch != " ":
        count += 1

print("Length without spaces:", count)
