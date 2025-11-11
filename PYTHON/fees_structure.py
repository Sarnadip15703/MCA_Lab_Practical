def CalculateSITcourseFees(course_code, TIGans, entrance_test, male):
    admission_fee = 0
    remaining_fee = 0
    semesters = 0

    # Course details
    if course_code == 1:
        admission_fee = 100000
        remaining_fee = 75000
        semesters = 8
    elif course_code == 2:
        admission_fee = 70000
        remaining_fee = 50000
        semesters = 8
    elif course_code == 3:
        admission_fee = 70000
        remaining_fee = 50000
        semesters = 8
    elif course_code == 4:
        admission_fee = 60000
        remaining_fee = 45000
        semesters = 6
    elif course_code == 5:
        admission_fee = 50000
        remaining_fee = 30000
        semesters = 6
    elif course_code == 6:
        admission_fee = 140000
        remaining_fee = 100000
        semesters = 4
    elif course_code == 7:
        admission_fee = 120000
        remaining_fee = 80000
        semesters = 4
    else:
        print("Invalid course code!")
        return

    # Apply scholarships
    if TIGans == 1:
        if course_code in [1, 2, 3, 4, 5]:  # UG Courses
            per_sem_scholar = 10000
        else:
            per_sem_scholar = 15000

        total_fees = (admission_fee - per_sem_scholar) + (semesters - 1) * (remaining_fee - per_sem_scholar)
    else:
        total_fees = admission_fee + (semesters - 1) * remaining_fee

        if entrance_test == 1:
            total_fees -= 15000

        if male == 0:
            total_fees -= 10000

    print("Total Course Fees: ₹", format(total_fees, ",.2f"))


# ---------- MAIN CODE ----------
print("---- SIT Course Fee Calculator ----")
print("1 for BTech")
print("2 for BCA")
print("3 for BBA")
print("4 for BHHA")
print("5 for BSc")
print("6 for MBA")
print("7 for MCA")

course_code = int(input("\nEnter Course Code (1-7): "))
TIGans = int(input("Are you from Techno India Group? (1 for Yes, 0 for No): "))
entrance_test = int(input("Have you qualified the entrance test? (1 for Yes, 0 for No): "))
male = int(input("Gender (1 for Male, 0 for Female): "))

CalculateSITcourseFees(course_code, TIGans, entrance_test, male)