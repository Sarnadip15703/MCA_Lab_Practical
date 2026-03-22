n = int(input("Enter no: "))

def isPrime(n):
    c = 0
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

a = 2
c = 0
l = []

for i in range(3, n+1):
    if isPrime(i):
        a += i
        if a % 2 != 0 and a <= n:
            c += 1
            l.append(a)

print(l)
print(c)