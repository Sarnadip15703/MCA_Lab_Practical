n = int(input("Enter 5 digits: "))
s = 0

a = (n // 10000) + 1
n = n % 10000
s = s + (a * 10000)

a = (n // 1000) + 1
n = n % 1000
s = s + (a * 1000)

a = (n // 100) + 1
n = n % 100
s = s + (a * 100)

a = (n // 10) + 1
n = n % 10
s = s + (a * 10)

a = n + 1
s = s + a

print(s)