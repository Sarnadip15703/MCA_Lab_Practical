''' The Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a program to 
convert this temperature into Centigrade degrees'''

# Take temperature input in Fahrenheit from the user
temp = float(input("Enter the temperature in Fahrenheit: "))

# Apply the conversion formula to convert Fahrenheit to Celsius
# Formula: Celsius = (5/9) * (Fahrenheit - 32)
c = (5/9) * (temp - 32)

# Display the converted temperature in Celsius
print("The temperature in centigrade is:", c)
