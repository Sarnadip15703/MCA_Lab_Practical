a = [1,2,3,4,5]
b = [10, 20, 30, 40, 50]
k = 2
newList = []

for i in range(k):
    newList.insert(0, a[len(a)-i-1])

newList.extend(a[0:len(a)-k])
for i, el in enumerate(b):
    newList[i] += el
    
print(newList)