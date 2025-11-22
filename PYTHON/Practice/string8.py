s = input("Enter a string: ")

# has_letter = False
# has_number = False

# for ch in s:
#     if ch.isalpha():
#         has_letter = True
#     elif ch.isdigit():
#         has_number = True

# if has_letter and has_number:
#     print("Contains letters and numbers")
has_letter_number =False
for ch in s:
    if ch.isalnum():
        has_letter_number = True
        print("Contains letters and numbers")
else:
    print("Invalid")
