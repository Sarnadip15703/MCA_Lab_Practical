'''If cost price and selling price of an item is input through the keyboard, write a program to
determine whether the seller has made profit or incurred loss. Also determine how much profit he
made or loss he incurred.'''

# Read cost price (CP) from user input and convert to integer
CP = int(input("Enter Cost price: "))

# Read selling price (SP) from user input and convert to integer
SP = int(input("Enter Selling price: "))

# If selling price is greater than cost price -> profit
if SP > CP:
    profit = SP - CP  # amount of profit
    print("The Seller made a profit of RS:", profit)

# If cost price is greater than selling price -> loss
elif CP > SP:
    loss = CP - SP  # amount of loss
    print("The Seller made a loss of RS:", loss)

# If neither, then there is no profit and no loss
else:
    print("No Profit, No Loss")