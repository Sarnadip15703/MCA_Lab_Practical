s=input("Enter the string:")
vis=""
for i in s:
    if i not in vis and i!=" ":
        freq=s.count(i)
        print("The frequency of",i,"is",freq)
        vis+=i