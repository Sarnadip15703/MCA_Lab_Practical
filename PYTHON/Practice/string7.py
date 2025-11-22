s = input("Enter a string: ")
words = s.split()

result = ""

for w in words:
    if len(w) == 1:
        result += w.upper() + " "
    else:
        new_word = w[0].upper() + w[1:-1] + w[-1].upper()
        result += new_word + " "

print("Result:", result)
