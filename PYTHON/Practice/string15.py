n = int(input("Enter number of strings: "))

strings = []
for i in range(n):
    strings.append(input("Enter string: "))

ch = input("Enter character to check frequency: ")

count = 0

for s in strings:
    count += s.count(ch)

print("Total frequency of character:", count)
