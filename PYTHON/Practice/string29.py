s = input("Enter string: ")
n = int(input("Enter rotation value: "))

rotated = s[n:] + s[:n]

print("Rotated string:", rotated)
