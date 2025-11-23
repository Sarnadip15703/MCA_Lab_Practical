''' Given n and an integer k, and then a list of n integers, print all the 
integers that are multiples of k, but skip the first one you encounter (i.e., don't print the 
first multiple found, but print any subsequent multiples).'''

# Input: number of elements to process
n = int(input("Enter the number of elements: "))
# Input: divisor k to check for multiples
k = int(input("Enter the divisor: "))

# Counter to track how many multiples of k have been found
count = 0
# String to store all multiples (except the first one) separated by spaces
numbers = ""

# Loop through n iterations to get integers
for i in range(n):
    # Input: get each number from user
    num = int(input("Enter a number: "))
    # Check if number is a multiple of k
    if num % k == 0:
        # Increment counter for multiples found
        count += 1
        # If this is not the first multiple (count > 1), add it to the result string
        if count > 1:
            # Append number and space to the numbers string
            numbers = numbers + str(num) + " "

# Print all multiples of k except the first one (space separated)
print(numbers)
