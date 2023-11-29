# LAB ASSIGNMENT 2
**Assigned date:** 7/8
**Due date:**  Sunday, July 12
**20 points**

## Objectives:

In this lab, you learn to create a Raptor flowchart.

After completing this lab, you will be able to:

* Plan the logic for a solution to a programming problem using a flowchart.
* Use Raptor software to create flowcharts
* Understand the magic numbers

## PreLab

Do the following activities before doing the lab assignment. 

* Read chapter 2.
* Do the homework assignment #2

## Problem 

Draw a flowchart (name the file as lab2.rap)  using Raptor to compute a person's income tax. Here is the relevant tax law:

* There is a flat tax rate of 20 percent
* There is a $10,000.00 standard deduction
* There is a $2000 additional deduction for each dependent

The user inputs are the gross income and number of dependents. The program calculates the income tax based on the inputs and the tax law and then displays the income tax.

**The user interface for the income tax program**

Enter the gross income:  500000.00
Enter the number of dependents: 4
The income tax is $96400.00
The gross income after-tax  $ 403600.0

## Requirements

There are no magic numbers in the flowchart.  Magic numbers are always constant in the program.  In the lab assignment, flat rate, $10,000, $2000 are constants. You need to create a named constant (constant variable) to represent the magic number. The named constants should be always written in uppercase.

Example: Define the constants using a named constant. A number that is not changed in a program should be assigned to a named constant. The named constant is sometimes called a constant variable. All the characters in a constant variable should be uppercase.

TAX_RATE = 0.2
STANDARD_DEDUCTION -= 10000.0
DEPENDENT_DEDUCTION = 2000.0

When you write an expression that has the magic number, you should replace it with the named constant.

Example:

TAX_RATE = 0.02
incomeTax = grossIncome * 0.02 - This expression has a magic number 0.02. You need to rewrite the expression with a named constant.

incomeTax = grossIncome * TAX_RATE

All the variable must be camel casing.

Hints:

* Input gross income, and number of dependents
* set TAX_RATE TO 0.2
* Set STANDARD_DEDUCTION to 10000.00
* Set DEPENDENT_DEDUCTION TO 2000.0
* Set the dependent deduction amount as DEPENDEN_DEDUCTION  times the number of dependents
* Set gross after deduction as subtracting the dependent deduction amount and STANDARD_DEDUCTION  (10000.0) from the gross income
* Set the income tax is gross after deduction times TAX_RATE
* Set the gross income after tax as subtracting income tax from the gross income
* Display the income tax
* Display the income tax
* Display gross income after tax

Zoom Video on how to  do the lab assignment 2  -   [Zoom video](https://cerritos.instructure.com/courses/42799/files/2477850/download?wrap=1)

## Grading

Name the Raptor flowchart file as **lab2.rap. Do not change the file name to any other name.** Submit the file to the Canvas. You don't have to do the pseudocode in this lab assignment.

