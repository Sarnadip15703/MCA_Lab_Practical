s = input("Enter string: ")
temp = s
count = 0

# for i in range(1, len(s)+1):
#     rotated = temp[i:i+len(s)]
while True:
    temp = temp[1:]+temp[0]
    count += 1
    if temp == s:
        break

print("Minimum rotations needed:", count)
