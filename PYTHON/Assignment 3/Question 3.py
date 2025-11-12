'''Write a program to read a sequence of integers until the end (or 
given length). Then produce a new list by selecting numbers according to this rule: you 
begin expecting an even number; when you encounter an even number you accept it, 
then switch expectation to odd; when you next encounter an odd number you accept it, 
switch expectation to even, and so on. If a number does not meet the current 
expectation you skip it and keep going. At the end print the accepted list. '''

n = int(input("Enter how many numbers you want to enter:"))
expect_even = True
numbers = ""
for i in range(n):
    num = int(input("Enter no.: "))
    if expect_even:
        if num % 2 == 0:
            numbers = numbers + str(num) + " "
            expect_even = False
    else:
        if num % 2 != 0:
            numbers = numbers + str(num) + " "
            expect_even = True
        
print(numbers)