s = input("Enter string: ")

count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        print(s[i-1], count, end=" ")
        count = 1

    # print(i, s.count(i))

print(s[-1], count)   # print last character count
