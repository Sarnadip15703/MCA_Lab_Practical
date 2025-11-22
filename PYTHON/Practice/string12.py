s = input("Enter a string: ")

min_count = len(s)
least_char = ""

for ch in s:
    c = s.count(ch)
    if c < min_count:
        min_count = c
        least_char = ch

print("Least frequent character:", least_char)
