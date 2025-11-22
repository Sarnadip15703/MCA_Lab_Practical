s=input("Enter the string number")

num=0
for ch in s:
    num=num*10+ ord(ch)-48
print("the converted integer is ",num)