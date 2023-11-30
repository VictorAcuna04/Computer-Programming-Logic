#Initialize celsius to 0
Celsius = 0
#Set A to represent 9.0/5
A = 9.0/5
# Set B to represent 32
B = 32
#Display the colum title "Celsius" and "Fahrenheit"
print("Celsius", "Fahrenheit")
#While Celsius is less than or equal to 15, determine fahrenheit for given number of celsius and display the celsius and fahrenehit. Fahrenheit is rounded to 2 decimal places and Celcius is incremented by 1 each time.
while Celsius <= 15:
    Fahrenheit = A * Celsius + B
    print(Celsius, "     ", "%.2f"% Fahrenheit)
    Celsius = Celsius + 1

    
