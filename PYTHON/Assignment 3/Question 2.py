''' Given n and an integer k, and then a list of n integers, print all the 
integers that are multiples of k, but skip the first one you encounter (i.e., don’t print the 
first multiple found, but print any subsequent multiples).'''

n = int(input("Enter the number of elements: "))
k = int(input("Enter the divisor: "))

count = 0
numbers = ""
for i in range(n):
    num = int(input( "Enter a number: "))
    if num % k == 0:
        count += 1
        if count > 1:
          numbers=numbers + str(num) + " "
print(numbers)
