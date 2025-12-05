# Input: read a line of text from user
s = input("Enter a string: ")

# Add space at end to process last word
s = s + " "

# Initialize current word buffer
word = ""

# Initialize counter for word length (do not use len())
word_length = 0

# Initialize result string to store even length words
result = ""

# Iterate through each character in string
for ch in s:
    # Check if character is not a space
    if ch != " ":
        # Add character to current word
        word = word + ch
        # Increment word length counter
        word_length = word_length + 1
    else:
        # Space encountered - end of current word
        # Check if word length is even and word is not empty
        if word_length > 0 and word_length % 2 == 0:
            # Add even length word to result
            result = result + word + " "
        
        # Reset word and counter for next word
        word = ""
        word_length = 0

# Print all even length words (space separated)
print(result)