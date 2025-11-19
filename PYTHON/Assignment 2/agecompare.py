'''Compare ages of three people and print who is youngest.

This script reads ages for Ram, Shyam and Ajay and prints the
name of the youngest. The original comparison logic is kept
as-is; comments explain each step.
'''

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