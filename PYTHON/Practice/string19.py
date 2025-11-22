s = input("Enter string: ")
k = int(input("Enter length k: "))

words = s.split()

for w in words:
    if len(w) > k:
        print(w)
