s = input("Enter string: ")
i = int(input("Enter index to remove: "))

# result = ""
# for index in range(len(s)):
#     if index != i:
#         result = result + s[index]

# print("Result:", result)
s1=s[:i]+s[i+1:]
print(s1)