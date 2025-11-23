# s = input("Enter a sentence: ")
# word = input("Enter word to find: ")

# words = s.split()

# for i in range(len(words)):
#     if words[i] == word:
#         print("Found at position:", i)
#         break
# else:
#     print("Word not found")
s=input("Enter sentence").split()
word= input("Enter word:")
print(s.index(word))