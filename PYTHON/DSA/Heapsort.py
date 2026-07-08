def heapify(H,i,n):
    largest=i
    left=2*i+1
    right=2*i+2
    if left<n and H[left]>H[largest]:
        largest=left
    if right<n and H[right]>H[largest]:
        largest=right
    if largest!=i:
        H[i],H[largest]=H[largest],H[i]
        heapify(H,largest,n)

def max_heap(A,n):
    for i in range(n//2 - 1, -1, -1):
        heapify(A,i,n)
    
if __name__ == "__main__":
    A = [40,30,50,60,35,49,65,55,25,28]
    max_heap(A, len(A))
    print(A)