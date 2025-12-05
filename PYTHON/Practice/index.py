s=input("enter the string")
l=len(s)
listl=[0]*l
print(listl)
for i in range (len(s)):
    j=i-1
    for ch in range (j,0,-1):
        if (s[i]==s[ch]):
            listl[i]=ch+1
            break
print(listl)

st=" "
l=[0]*len(st)
for i in range(0,len(st)):
    for j in range(i-1,-1,-1):
        if st[i]==st[j]:
            l[i]=j+1
            break
print(l)
