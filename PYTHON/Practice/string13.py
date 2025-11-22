s = input("Enter a string: ")

max_count = 0
max_char = ""

for ch in s:
    c = s.count(ch)
    if c > max_count:
        max_count = c
        max_char = ch

print("Maximum frequency character:", max_char)
