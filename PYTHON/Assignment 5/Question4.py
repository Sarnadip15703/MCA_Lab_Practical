# l = [10, 45, 34, 43, 56, 57, 35]
l = [1, 2, 3, 4, 5]
k = 3

def avg(l):
    s = 0
    for el in l:
        s += el
    return s/len(l)
        
def varience(l):
    x = avg(l)
    s = 0
    
    for i in l:
        s += (i-x)**2
        
    return s/len(l)

ans = []
for i in range(len(l)-k+1):
    a = avg(l[i:i+k])
    v = varience(l[i:i+k])
    
    ans.append(tuple((a, v)))
print(ans)