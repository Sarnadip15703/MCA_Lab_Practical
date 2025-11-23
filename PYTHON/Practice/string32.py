n = int(input("Enter number of strings: "))
strings = []

for i in range(n):
    strings.append(input("Enter string: "))

k = input("Enter character: ")

strings.sort(key=lambda x: x.count(k))

print("Sorted list:", strings)
