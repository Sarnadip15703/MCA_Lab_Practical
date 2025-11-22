s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

count = 0

for ch in s1:
    if ch in s2:
        count += 1

print("Matching characters count:", count)

