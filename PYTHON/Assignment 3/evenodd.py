''' Given a list of integers, compute two sums: one for all even 
numbers, and one for all odd numbers. Then print both sums.'''

n=int(input("Enter any number"))
sum_even=0
sum_odd=0
for i in range(n):
    num=int(input("enter n: "))
    if num%2==0:
        sum_even+=num
    else:
        sum_odd+=num

print(sum_even,sum_odd)    
          
