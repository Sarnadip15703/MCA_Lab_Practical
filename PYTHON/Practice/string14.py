s = input("Enter a string: ")

print("Characters with odd frequency:")

for ch in s:
    if s.count(ch) % 2 != 0:
        print(ch)
