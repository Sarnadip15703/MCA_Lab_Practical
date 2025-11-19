'''Simple insurance premium eligibility and premium calculator.

Inputs:
- health: 'Excellent' or 'Poor'
- age: integer
- location: 'city' or 'village'
- gender: 'male' or 'female'

Based on these inputs the script prints premium and policy limits,
or indicates the person cannot be insured.
'''

# Read user details
health = input("Enter health (Excellent or Poor): ")
age = int(input("Enter the age: "))
location = input("Enter location (city or village): ")
gender = input("Enter gender (male or female): ")

# Eligibility: only people aged between 25 and 35 are considered
if age >= 25 and age <= 35:

    # Excellent health + city
    if health == "excellent":
        if location == "city":
            if gender == "male":
                print("premium is 4 thousand and policy amount cannot exceed 2 lakh")
            elif gender == "female":
                print("premium is 3 thousand and policy amount cannot exceed 1 lakh")

    # Poor health + village -> different premium
    elif health == "poor" and location == "village":
        print("premium is 6 thousand and policy amount cannot exceed 10,000")

else:
    # Age not in eligible range
    print("The person cannot be insured")