''' Given a list of integers, compute two sums: one for all even 
numbers, and one for all odd numbers. Then print both sums.'''

# Input: number of integers to process
n = int(input("Enter any number: "))

# Initialize sum for even numbers
sum_even = 0

# Initialize sum for odd numbers
sum_odd = 0

# Loop through n iterations to get integers
for i in range(n):
    # Input: get each number from user
    num = int(input("Enter n: "))
    
    # Check if number is even (divisible by 2)
    if num % 2 == 0:
        # Add to even sum
        sum_even += num
    else:
        # Add to odd sum
        sum_odd += num

# Print both sums: even sum first, then odd sum (space separated)
print(sum_even, sum_odd)

