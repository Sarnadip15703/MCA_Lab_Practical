# with open("input.txt","r") as file:
 
#  for i in file:
    
# #     print(file1)

#   # file.write (f"{}intitem and sum={sum}")
#   # file.write(l)


def bs(list,key):
    l=0
    h=l(list)-1
    while l<=h:
        m=(l+h)//2
        if list[m]==key:
            return m
        elif list[m]<key:
            l=m+1
        else:
            h=m-1
        return -1
li=[12,13,14,45,68,90]
k=68
result=bs(li,k)
print(result)