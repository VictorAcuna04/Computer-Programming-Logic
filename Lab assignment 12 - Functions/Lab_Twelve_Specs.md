# LAB ASSIGNMENT 12
**Assigned date:** Monday 8/3
**Due date:**  Sunday 8/9
**20 points**

## Objectives:

After completing this lab, you will be able to:

* Create and call a function
* Use a loop

## PreLab

* Read Python Tutor
  * while loop
  * Function

## Problem

Recall that we wrote a program to convert from Fahrenheit to Celsius. Let's say we want to print out a table with the temperatures in Fahrenheit from 0 to 100 in steps of 10 along with their Celsius equivalents. First, we can write a function that converts from Fahrenheit to Celsius.

The function has one parameter. The variable tempF represents the temperature in Fahrenheit. The function then uses that to compute the corresponding Celsius temperature. The last statement returns this result as its answer. Now we can write a program that uses this function, calling it with each Fahrenheit temperature from 0 to 100 in steps of 10.

The formula for converting a temperature from Fahrenheit to Celsius :

C =   5/9*(F-32)

Hint:

    def f_to_c(tempF):
         #Convert fahrenheit temperature to celsius temperature
        tempC = __________________
         return ______________
    
    def main():
          #Display "F               C  "
           print (_______________________________)
           fahrenheit_temp = 0
          while fahrenheit_temp __________________:       
    
                     #call the function f_to_c
                      celsius_temp = _________________________________
    
                     # display fahrenheit temperature and celsius temperature. Format celsius temperature to 2 decimal places.
                      print (__________________________________________________)
    
                     #Increment fahrenheit temperature by some value
                       fahenheit_temp = ______________________________
    
    #call the function main       

Output
| F | C |
| - | - |
| 0 | -17.78 |
| 10 | -12.22 |
| 20 | -6.67 |
| 30 | -1.11 |
| 40 | 4.44 |
| 50 | 10.00 |
| 60 | 15.56 |
| 70 | 21.11 |
| 80 | 26.67 |
| 90 | 32.22 |
| 100 | 37.78 |

## Grading

Submit the file lab12.py  to the Canvas. Do not change the file name to any other names.
