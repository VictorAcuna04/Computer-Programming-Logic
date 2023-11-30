# LAB ASSIGNMENT 10
**Due date:**  Thursday, August 6

**20 points**

Objectives:

After completing this lab, you will be able to:

* Validate input with a loop
* Using a counter controlled loop to keep track of the number of user inputs.
* Using a loop to accumulate totals

## PreLab

* Read chapter 4 (Logic Design book)  Making Selections within Ranges on pages 148-153
* Read chapter 5 (Logic Design book) Using a Definite Loop with a Counter (pages 172-173) and Using a loop to accumulate the totals (pages 194-198)
* Review the lecture note "Accumulation" in week 4.

## Problem

Create a Raptor flowchart to represent the logic of a program that asks the user to enter four test scores. The program displays the grade for each test score and the average of all four test scores. Use a loop to input four test scores. Validate the input. The test scores must be between 0 and 100. If the user enters a test score out of range 0 to 100, the flowchart asks the user to enter another input until the input is in the range. Use the grading table below to assign a grade to the test score.

| Test Score Average | Letter Grade |
| ------------------ | ------------ |
| 90-100 | A |
| 80-89 | B |
| 70-79 | C |
| 60-69 | D |
| Below 60 | F |

##
**Input**

Enter a test score: 55

Enter a test score: 96

Enter a test score: 73

Enter a test score: 82

##
**Output**
Test score: 55

Letter grade : F

Test score: 96

Letter grade : A

Test score: 73

Letter grade : C

Test score: 82

Letter grade : B

Test score average = 76.5000


**Hint:** pseudocode

    i= 1
    
    sum = 0
    
      while num <= 4
    
           input score
           
           if grade < 60
           
                grade = "F"
                
          else
          
                if average < 70
                
                     grade = "D"
                     
               else
               
                    if average < 80
    
                          grade = "C"
                          
                   else
                   
                         if average < 90
                         
                             grade =  "B"
                             
                        else 
                        
                             grade = "A"
                             
                        endif
                        
                   endif
                   
              endif  
              
         endif
         
     sum = sum + score
     
    i = i + 1
    
    end while
    
    average = sum/4
    
    display average
    
    end

## Grading

## Online Class
* Submit the file lab10.rap  to the Canvas. Do not change the file name to any other names.
