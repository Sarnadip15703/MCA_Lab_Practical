target=input("Enter target")

attemt=""
attempts=0
while attemt!=target:
    attemt=input("Enter guess")
    attempts+=1
print("matched in",attempts)
   