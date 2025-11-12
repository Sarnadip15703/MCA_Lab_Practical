health = input("Enter health (Excellent or Poor): ")
age = int(input("Enter the age: "))
location = input("Enter location (city or village): ")
gender = input("Enter gender (male or female): ")

# if health == "excellent" and  age >= 25 and age <= 35 and location == "city" and gender == "male":
#     print("premium is 4 thousand and policy amount cannot exceed 2 lakh")
# elif health == "excellent" and age >= 25 and age <= 35 and location == "city" and gender == "female":
#     print("premium is 3 thousand and policy amount cannot exceed 1 lakh")
# elif health == "poor" and age >= 25 and age <= 35 and location == "village" and gender == "male":
#     print("premium is 6 thousand and policy amount cannot exceed 10,000")
# else:
#     print("The person cannot be insured")

if age >= 25 and age <= 35:

    if health == "excellent":
        if location == "city":
            if gender == "male":
                print("premium is 4 thousand and policy amount cannot exceed 2 lakh")
            elif gender == "female":
                print("premium is 3 thousand and policy amount cannot exceed 1 lakh")
    
    elif health == "poor" and location == "village":
        print("premium is 6 thousand and policy amount cannot exceed 10,000")
        
else:
    print("The person cannot be insured")