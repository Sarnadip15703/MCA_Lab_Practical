'''Write a program that repeatedly asks the user for a positive integer. 
For each integer, compute the “digit sum” (sum of its digits). If that digit sum is greater 
than 9, take that result and again compute its digit sum, continue until the result is a 
single digit (≤ 9). Print the number of iterations it took and the final single-digit result. 
Repeat this entire process for each integer entered until the user enters zero or a 
negative number to stop. At the end, print how many integers were processed. '''

def add_digit(num):
    add = 0
    while num > 0:
        add += num % 10
        num = num // 10
    return add

count = 0  # To count how many positive numbers processed

while True:
    num = int(input("Enter a positive integer (0 or negative to stop): "))
    
    if num <= 0:
        break  # Stop if 0 or negative
    count += 1

    iterations = 0
    digit_sum = num

    # Keep finding digit sum until it becomes a single digit
    while digit_sum > 9:
        digit_sum = add_digit(digit_sum)
        iterations += 1

    print("Iterations:", iterations, ", Final digit:", digit_sum)

print("Total numbers processed:", count)