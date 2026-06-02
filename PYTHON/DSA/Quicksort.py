def quick_sort(a,l,r):
    if l<r:
        p=quick(a,l,r)
        quick_sort(a,l,p-1)
        quick_sort(a,p+1,r)
def quick(a,l,r):
    p=l
    left=l+1
    right=r
    while True:
        while a[p]<=a[right]and right>=left:
            right=right-1
        if a[p]>a[right]:
            a[p],a[right] = a[right],a[p]
            p=right
            right=right-1
        if right<left:
            return p
        while a[p]>=a[left] and right>=left:
            left=left+1
        if a[p]<a[left]:
            a[p],a[left] = a[left],a[p]
            p=left
            left=left+1
        if right<left:
            return p
a=[0,17,-3,90,0]
quick_sort(a,0,len(a)-1)
print("sorted array is",a)