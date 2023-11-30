#Define f_to_c to represent the formula to represent the conversion from fahrenheit to celsius
def f_to_c(tempF):
    tempC = (5/9) * (tempF - 32)
    return tempC
#Point of execution of program
def main():
#Display Fahrenheit and Celsius
    print ("F", "\t", "C")
#List Fahrenheit section 11 times
    for x in range(11):
#Convert fahrenheit to celsius
        celsius_temperature = f_to_c(x*10)
#Display numbers 0-100, starting with 0, and then skip counting by 10 for the Fahrenheit section. The Celsius temperature is also displayed
        print (x*10, "\t", "{:.2f}".format(celsius_temperature))
main()
    
