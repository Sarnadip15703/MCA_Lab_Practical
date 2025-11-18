#taking input
c=1
while c<11:
    hours=int(input("how many hours the employee worked"))
    if(hours>40):
        overtime=hours-40
        fees=overtime*12
        print("The extra money to be paid i  s",fees)
    else:
        print("no overtime")
    c+=1  
    
