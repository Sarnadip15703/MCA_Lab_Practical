s = input("Enter a string: ")

half = len(s) // 2   # middle index

first = s[:half]     # first half
second = s[half:]    # second half

result = first + second.upper()

print("Result:", result)