'''An Insurance company follows following rules to calculate premium.
● If a person’s health is excellent and the person is between 25 and 35 years of age and lives in a
city and is a male then the premium is Rs. 4 per thousand and his policy amount cannot exceed
Rs. 2 lakhs.
● If a person satisfies all the above conditions except that the sex is female then the premium is
Rs. 3 per thousand and her policy amount cannot exceed Rs. 1 lakh.
● If a person’s health is poor and the person is between 25 and 35 years of age and lives in a village
and is a male then the premium is Rs. 6 per thousand and his policy cannot exceed Rs. 10,000.
● In all other cases the person is not insured.
Write a program to output whether the person should be insured or not, his/her premium rate and
maximum amount for which he/she can be insured'''

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