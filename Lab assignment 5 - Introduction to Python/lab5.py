#input the height
sHeight= input("Input the height: ")
height = float(sHeight)
#input the width
width = float(input("Enter the width: "))
#determine the area
area = height * width
#determine the gallons
SQUARE_FEET_PER_GALLON = 150
gallons = area / SQUARE_FEET_PER_GALLON
#display the output
print("The gallons needed is ", gallons, " gallons.")
