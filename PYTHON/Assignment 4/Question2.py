# s=input("Enter a string")
# digits=""
# count=0
# for ch in s:
#     if ch.isdigit():
#        digits.append(ch)
# if count==0:
#     print("No digits found")
# else:
#     add=int(ch)
s = input("Enter a string: ")

digits = []

# Extract digits
for ch in s:
    if ch.isdigit():        
        digits.append(int(ch))   
if len(digits) == 0:
    print("No digits found in the string.")
else:
    total = sum(digits)
    avg = total / len(digits)
    maximum = max(digits)
    minimum = min(digits)

    print("Sum =", total)
    print("Average =", avg)
    print("Maximum =", maximum)
    print("Minimum =", minimum)
