words=input("Enter number words").split()
nums=""

for w in words:
    if w=="zero": nums+="0"
    elif w=="one": nums+="1"
    elif w=="two": nums+="2"
    elif w=="three": nums+="3"
    elif w=="four": nums+="4"
    elif w=="five": nums+="5"
    elif w=="six": nums+="6"
    elif w=="seven": nums+="7"
    elif w=="eight": nums+="8"
    elif w=="nine": nums+="9"
print(nums)