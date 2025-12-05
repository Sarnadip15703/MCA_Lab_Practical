a = input("Enter first string (a): ")
b = input("Enter second string (b): ")

missing = []

# Check each character of a in b
for ch in a:
    if ch not in b:     
        missing.append(ch)

# Output results
if len(missing) == 0:
    print("True")        # all characters are present
else:
    print("False")       # some characters are missing
    print("Missing characters:", missing)
