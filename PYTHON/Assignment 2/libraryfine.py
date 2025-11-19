'''Calculate library fine based on number of overdue days.

Rules (as implemented):
- 0-5 days: pay fifty paise
- 6-10 days: pay one rupee
- 11-29 days: pay five rupees
- 30 or more: membership cancelled
'''

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