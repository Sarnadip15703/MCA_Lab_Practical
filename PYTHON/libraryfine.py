days=int(input("Enter the number of days"))

if(days<=5):
    print("Pay a fine of fifty Paise")
elif(days<=10):
    print("Pay a fine of one rupees")
elif(days>10 and days<30):
    print("Pay a fine of five rupees")
else:
    print("Membership Cancelled")