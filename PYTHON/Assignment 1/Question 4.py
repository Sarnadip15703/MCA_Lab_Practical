''' A cashier has currency notes of denominations 10, 50 and 100. If the amount to be
 withdrawn is input through the keyboard in hundreds, find the total number of currency
notes of each denomination the cashier will have to give to the withdrawer. '''

# Input: amount to be withdrawn
a = int(input("Enter the amount"))

# Calculate number of 100 notes and remaining amount
b = a // 100
a = a % 100

# Calculate number of 50 notes and remaining amount
c = a // 50
a = a % 50

# Calculate number of 10 notes and remaining amount
d = a // 10
a = a % 10

# Print number of 100 denomination notes
print("Number of 100 notes:", b)

# Print number of 50 denomination notes
print("Number of 50 notes:", c)

# Print number of 10 denomination notes
print("Number of 10 notes:", d)
