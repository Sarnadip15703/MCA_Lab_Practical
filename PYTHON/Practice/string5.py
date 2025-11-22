s = input("Enter string: ")
words = s.split()

for w in words:
    if len(w) % 2 == 0:
        print(w)
