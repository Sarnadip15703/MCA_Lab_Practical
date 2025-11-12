''' Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic 
salary, and house rent allowance is 20% of basic salary. Write a program to calculate his gross 
salary.'''

# Take basic salary input from the user
basicsalary = int(input("Enter salary: "))

# Calculate Dearness Allowance (DA) - 40% of basic salary
da = (basicsalary * 40) / 100

# Calculate House Rent Allowance (HRA) - 20% of basic salary
hra = (basicsalary * 20) / 100

# Calculate total gross salary (Basic Salary + DA + HRA)
totalsalary = (basicsalary + da + hra)

# Display the total gross salary
print("Total Salary is:", totalsalary)
