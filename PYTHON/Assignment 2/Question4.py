'''A library charges a fine for every book returned late. For first 5 days the fine is 50 paise, 
for 6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book after 
30 days your membership will be cancelled. Write a program to accept the number of days the 
member is late to return the book and display the fine or the appropriate message'''

# Read number of overdue days
days = int(input("Enter the number of days: "))

# Determine fine or cancellation based on ranges
if (days <= 5):
    print("Pay a fine of fifty Paise")
elif (days <= 10):
    print("Pay a fine of one rupees")
elif (days > 10 and days < 30):
    print("Pay a fine of five rupees")
else:
    print("Membership Cancelled")