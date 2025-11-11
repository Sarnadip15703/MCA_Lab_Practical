graduation=input("Do you have Graduation?(y/n)")
marks=float(input("Enter your Graduation marks"))
math_grad=float(input("Enter your maths mark in Graduation(if not available,enter 0)"))
math_hs=float(input("Enter your maths mark in HS(if not available,enter 0)"))
caste =input("Enter your caste(G for general/SC/ST?OBC)")

if (graduation=='y'and caste=="G"and marks>=50 and (math_hs>=50 or math_grad>=50))or(graduation=="y"and caste=="SC","ST","OBC" and marks>=45 and (math_hs>=50 or math_grad>=50)):
    print ("Eligible for MCA")
else:
    print("Not Eligible for MCA")