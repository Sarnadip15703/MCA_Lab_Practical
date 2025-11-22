n=input("Enter the string:")
val=0
for i in n:
    val=val*10+(ord(i)-48)
print("The numeric value is",val)
