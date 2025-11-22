binary = input("Enter binary number: ")
decimal = 0

for bit in binary:
    decimal = decimal * 2 + (ord(bit) - 48)
print("Decimal value:", decimal)