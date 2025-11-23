'''Write a program to read a sequence of integers until the end (or 
given length). Then produce a new list by selecting numbers according to this rule: you 
begin expecting an even number; when you encounter an even number you accept it, 
then switch expectation to odd; when you next encounter an odd number you accept it, 
switch expectation to even, and so on. If a number does not meet the current 
expectation you skip it and keep going. At the end print the accepted list. '''

# Input: number of integers to process
n = int(input("Enter how many numbers you want to enter:"))
# Flag to track whether we are expecting an even number (start with True)
expect_even = True
# String to store accepted numbers separated by spaces
numbers = ""

# Loop through n iterations to get integers
for i in range(n):
    # Input: get each number from user
    num = int(input("Enter no.: "))
    # Check if we are currently expecting an even number
    if expect_even:
        # If number is even, accept it
        if num % 2 == 0:
            # Append number and space to the numbers string
            numbers = numbers + str(num) + " "
            # Switch expectation to odd for next number
            expect_even = False
    else:
        # We are expecting an odd number
        # If number is odd, accept it
        if num % 2 != 0:
            # Append number and space to the numbers string
            numbers = numbers + str(num) + " "
            # Switch expectation to even for next number
            expect_even = True

# Print the accepted list of numbers (space separated)
print(numbers)