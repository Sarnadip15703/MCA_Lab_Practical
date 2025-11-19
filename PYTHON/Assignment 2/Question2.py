'''If the ages of Ram, Shyam and Ajay are input through the keyboard, write a program to
determine the youngest of the three.'''

# Read ages as integers
Ram = int(input("Enter Ram's age: "))
Shyam = int(input("Enter Shyam's age: "))
Ajay = int(input("Enter Ajay's age: "))

# The following conditional selects who is youngest. The code
# preserves the original conditions and only documents intent.
if (Ram and Shyam>Ajay):
    print ("Ajay is Youngest")
elif(Ram>Shyam):
    print("Shyam is Youngest")
else:
    print("Ram is Youngest")