length=int(input("Enter the Length"))
breadth=int(input("Enter the breadth"))

area=length*breadth
perimeter=2*(length+breadth)

if(area>perimeter):
    print("The area of rectangle is greater than its perimeter")
else:
    print("The perimeter of rectangle is greater than its area")