'''Problem: SIT Course Fees
Siliguri Institute of Technology has started its admission process for the academic session 2026.
Admission fees vary for the different courses offered by the institute.'''

def CalculateSITcourseFees(course_code, TIGans, entrance_test, male):
    # Initialize fee variables
    admission_fee = 0
    remaining_fee = 0
    semesters = 0

    # Set course-specific fee values and semester counts
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

    # Apply scholarships or discounts depending on TIGans status
    if TIGans == 1:
        # TIG candidates get a per-semester scholarship
        if course_code in [1, 2, 3, 4, 5]:  # UG Courses
            per_sem_scholar = 10000
        else:
            per_sem_scholar = 15000

        total_fees = (admission_fee - per_sem_scholar) + (semesters - 1) * (remaining_fee - per_sem_scholar)
    else:
        # Regular fee calculation
        total_fees = admission_fee + (semesters - 1) * remaining_fee

        # Apply entrance test discount if applicable
        if entrance_test == 1:
            total_fees -= 15000

        # Apply gender-based discount for female (male==0 means female here)
        if male == 0:
            total_fees -= 10000

    # Print the computed total fee formatted with comma separators
    print("Total Course Fees: ₹", format(total_fees, ",.2f"))


# ---------- MAIN CODE (CLI) ----------
print("---- SIT Course Fee Calculator ----")
print("1 for BTech")
print("2 for BCA")
print("3 for BBA")
print("4 for BHHA")
print("5 for BSc")
print("6 for MBA")
print("7 for MCA")

# Gather inputs from the user and call the calculation function
course_code = int(input("\nEnter Course Code (1-7): "))
TIGans = int(input("Are you from Techno India Group? (1 for Yes, 0 for No): "))
entrance_test = int(input("Have you qualified the entrance test? (1 for Yes, 0 for No): "))
male = int(input("Gender (1 for Male, 0 for Female): "))

CalculateSITcourseFees(course_code, TIGans, entrance_test, male)