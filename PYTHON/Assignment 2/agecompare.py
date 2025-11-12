Ram=int(input("Enter Ram's age:"))
Shyam=int(input("Enter Shyam's age:"))
Ajay=int(input("Enter Ajay's age:"))

if (Ram and Shyam>Ajay):
    print ("Ajay is Youngest")
elif(Ram>Shyam):
    print("Shyam is Youngest")
else:
    print("Ram is Youngest")