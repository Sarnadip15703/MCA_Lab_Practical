'''If the marks obtained by a student in five different subjects are input through the keyboard, find 
out the aggregate marks and percentage marks obtained by the student. Assume that the 
maximum marks that can be obtained by a student in each subject is 100. '''

# Input marks for 5 subjects from the user
sub1 = int(input("Enter marks of sub1: "))
sub2 = int(input("Enter marks of sub2: "))
sub3 = int(input("Enter marks of sub3: "))
sub4 = int(input("Enter marks of sub4: "))
sub5 = int(input("Enter marks of sub5: "))

# Calculate total marks of all 5 subjects
totalmarks = (sub1 + sub2 + sub3 + sub4 + sub5)

# Calculate average marks (percentage) by dividing total by number of subjects
averagemarks = (totalmarks) / 5

# Display the average marks (percentage)
print("The percentage marks is", averagemarks)

# Display the total aggregate marks
print("The aggregate marks is", totalmarks)
         
