'''If cost price and selling price of an item is input through the keyboard, write a program to 
determine whether the seller has made profit or incurred loss. Also determine how much profit he 
made or loss he incurred'''

CP=int(input("Enter Cost price"))
SP=int(input("Enter Selling price"))

if(SP>CP):
    profit=SP-CP
    print("The Seller made a profit of RS:",profit)
elif(CP>SP):
    loss=CP-SP
    print("The Seller made a loss of RS:",loss)
else:
    print("No Profit,No Loss")