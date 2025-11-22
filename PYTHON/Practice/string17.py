s = input("Enter a string: ")

special_found = False

for ch in s:
    if not ch.isalnum():   
        special_found = True
        break

if special_found:
    print("Contains special characters")
else:
    print("Does not contain special characters")
