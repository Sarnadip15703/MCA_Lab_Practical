s1=input("Enter the first string: ")
s2=input("Enter the second string: ")

i=0
j=len(s2)-1
result=""
while i < len(s1) and j >= 0:
    result=result+s1[i]+s2[j]
    i=i+1
    j=j-1

if len(s1) > len(s2):
    result=result+s1[i:] 
elif len(s2) > len(s1):
    result=result+s2[:j]   
print("The merged string is:", result)

