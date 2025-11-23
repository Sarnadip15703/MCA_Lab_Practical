s = input("Enter string: ")
sub = input("Enter substring to delete: ")

while sub in s:
    s = s.replace(sub, "")
# while len(s)>1 and s[0] == s[-1]:
#     s=s[1:-1]

if s == "":
    print("String can become empty")
else:
    print("Cannot be empty, remaining:", s)
