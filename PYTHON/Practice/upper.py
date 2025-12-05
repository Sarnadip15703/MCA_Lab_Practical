# Input: get string from user
string = input("Enter a string: ")

# Initialize counter to find length of string
length = 0
# Loop through each character to count length
for char in string:
    length = length + 1

# Calculate the midpoint of the string
mid = length // 2

# Initialize result string with first half (unchanged)
result = ""

# Loop through first half of string
for i in range(mid):
    result = result + string[i]

# Loop through second half of string and convert to uppercase manually
for i in range(mid, length):
    # Get character at position i
    char = string[i]
    # Convert character to uppercase manually using ASCII values
    if char >= 'a' and char <= 'z':
        # Convert lowercase to uppercase by subtracting 32 from ASCII value
        char = chr(ord(char) - 32)
    # Append uppercase character to result
    result = result + char

# Print the result with first half in original case and second half in uppercase
print(result)