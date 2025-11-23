s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

w1 = s1.split()
w2 = s2.split()

print("Uncommon words:")

for w in w1:
    if w not in w2:
        print(w)

for w in w2:
    if w not in w1:
        print(w)
