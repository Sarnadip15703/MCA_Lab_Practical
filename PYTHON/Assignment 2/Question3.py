'''Given the length and breadth of a rectangle, write a program to find whether the area of the
rectangle is greater than its perimeter. For example, the area of the rectangle with length = 5 
and breadth = 4 is greater than its perimeter.'''

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