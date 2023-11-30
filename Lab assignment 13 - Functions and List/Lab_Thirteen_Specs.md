# LAB ASSIGNMENT 13
**Due date:**   Tuesday 8/11

**20 points**

**We have 13 lab assignments, I will drop one lab assignment that has the lowest score or the one you did not submit. If you think your 12 lab assignments are good, then you don't have to do the lab assignment 13.
This lab assignment is due on Tuesday, August 11.**

## Problem 

The Weather Service Bureau department has data representing monthly rainfall for a year and we would like to create a table categorizing each month as rainy (rainfall 20% higher than average) dry (rainfall 25% lower than average) or average. The data file for monthly rainfall is called rainfall.txt Download rainfall.txt.

rainfall.txt

    95
    100
    120
    130
    135
    145
    155
    185
    190
    160
    130
    120
    
Store the data file in the same folder as your lab13.py.

## Output

The year's average monthly rainfall was 139 mm.

September has the highest rainfall (190 mm).

January has the lowest rainfall (95 mm)

| Month | Rainfall (mm) | Classification |
|-------|---------------|--------------|
| Jan | 95 | Dry |
| Feb | 100 | Dry |
| Mar | 120 | Average |
| Apr | 130 | Average |
| May | 135 | Average |
| Jun | 145 | Average |
| Jul | 155 | Average |
| Aug | 185 | Rainy |
| Sep | 190 | Rainy |
| Oct | 160 | Average |
| Nov | 130 | Average |
| Dec | 120 | Average |

## Program Requirements:

Implement the following functions in the program:

    def largestRainfall(arr,n)
    
    # arr is a list of rainfall and n is number of months
    #return the highest rainfall
    #display
    
    def smallest(arr,n):
    
    # arr is a list of rainfall and n is number of months
    #return the lowest rainfall 
    
    def averageRainfall(arr,n):
    
    # arr is a list of rainfall and n is number of months
    #return the average rainfall 
    
    def ClassifyAndDisplayRainfall(arr,n):
    
    # arr is a list of rainfall and n is number of months
    #display the table with columns month, rainfall, and classification
    
    def main():
    
    #open the file rainfall.txt
    #load the rain falls into a list
    
    #display the highest rainfall, the lowest rainfall, and the average rainfall
    #display the table with columns month, rainfall, and classification

Down load the file lab13.py Download lab13.py and store it in the same folder that has the file rainfall.tx. Open the file and review the code. You need to complete the program by filling in the blanks. After you test the program successfully, you submit lab13.py to the Canvas. You don't need to upload the file rain.txt.
