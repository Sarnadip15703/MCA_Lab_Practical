s = input("Enter string: ")
i = int(input("Enter index to remove: "))

# result = ""

# for index in range(len(s)):
#     if index != i:
#         result += s[index]

# print("New string:", result)
print(s[:i]+s[i+1:])