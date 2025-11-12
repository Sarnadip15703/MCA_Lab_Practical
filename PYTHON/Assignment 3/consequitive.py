'''Input a sequence of 8 integers, count how many blocks of 
consecutive increasing numbers exist. A block is defined as one or more numbers such 
that each number after the first in the block is strictly greater than its predecessor. For 
example [2, 3, 5, 1, 2, 3, 3, 4] has: first block [2,3,5], then second block [1,2,3], skip the 
3 to 3 since not strictly greater, then third block [3,4]. So the answer would be 3. Also print 
the length of the longest block.'''

# Take 8 integers as input using loop
print("Enter 8 integers:")

block_count = 0
current_length = 1
longest = 1

# Take the first number separately
prev = int(input())
count = 1  # to track how many numbers read

while count < 8:
    num = int(input())
    count += 1

    if num > prev:
        current_length += 1
    else:
        block_count += 1
        if current_length > longest:
            longest = current_length
        current_length = 1

    prev = num

# Handle last block
block_count += 1
if current_length > longest:
    longest = current_length

print("Number of increasing blocks:", block_count)
print("Length of the longest block:", longest)