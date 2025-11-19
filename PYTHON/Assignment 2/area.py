'''Calculate and compare area and perimeter of a rectangle.

Reads `length` and `breadth` from the user, computes area and
perimeter, then prints which value is greater.
'''

# Read rectangle dimensions
length = int(input("Enter the Length: "))
breadth = int(input("Enter the Breadth: "))

# Compute area and perimeter
area = length * breadth
perimeter = 2 * (length + breadth)

# Compare and print a clear message
if (area > perimeter):
    print("The area of rectangle is greater than its perimeter")
else:
    print("The perimeter of rectangle is greater than its area")