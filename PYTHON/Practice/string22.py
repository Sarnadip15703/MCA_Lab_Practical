n = int(input("Enter number of words in list: "))

words = []
for i in range(n):
    words.append(input("Enter word: "))

target = input("Enter word to match: ")

print("Close matches:")

for w in words:
    if w[0] == target[0]:   # very simple matching logic
        print(w)
