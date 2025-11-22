s = input("Enter a string: ").lower()

vowels = "aeiou"
found = True

for v in vowels:
    if v not in s:
        found = False
        break

if found:
    print("String contains all vowels")
else:
    print("String does not contain all vowels")
