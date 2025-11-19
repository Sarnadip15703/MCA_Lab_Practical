'''MCA Course Admission Eligibility Check
    i)Graduation
    ii)50% marks in Graduation
    iii)Math with 50% marks either in HS or Graduation
'''

# Ask whether the applicant has completed graduation
graduation = input("Do you have Graduation?(y/n)")

# Graduation marks (percentage or marks as float)
marks = float(input("Enter your Graduation marks: "))

# Maths marks in graduation (enter 0 if not applicable)
math_grad = float(input("Enter your maths mark in Graduation (if not available, enter 0): "))

# Maths marks in higher secondary (enter 0 if not applicable)
math_hs = float(input("Enter your maths mark in HS (if not available, enter 0): "))

# Caste category: used to apply different eligibility cutoffs
caste = input("Enter your caste (G for general / SC/ST/OBC): ")

# NOTE: The original logic uses a compound boolean condition to
# determine eligibility. We keep the logic unchanged and only add
# comments here. The condition checks for general vs reserved
# category cutoffs and presence of a maths score >= 50 in either
# HS or graduation.
if (graduation=='y'and caste=="G"and marks>=50 and (math_hs>=50 or math_grad>=50))or(graduation=="y"and caste=="SC","ST","OBC" and marks>=45 and (math_hs>=50 or math_grad>=50)):
    print ("Eligible for MCA")
else:
    print("Not Eligible for MCA")