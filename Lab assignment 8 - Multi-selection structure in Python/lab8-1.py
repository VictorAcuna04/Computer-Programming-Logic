# Constants for the bonus thresholds
RANGE1=1000
RANGE2=3000
RANGE3=6000
BONUS0=0
BONUS1=25
BONUS2 = 50
BONUS3 = 100
BONUS4 = 200

#User inputs the first and last name. This years unit and last years units/
lastName = input("Enter last name: ")
firstName = input("Enter first name: ")
thisYear = int(input("Enter this year's units: "))
lastYear = int(input("Enter last year's units: "))

if thisYear < lastYear:
    bonus = 0
elif thisYear <= RANGE1:
    bonus = 25
elif thisYear <= RANGE2:
    bonus = 50
elif thisYear <= RANGE3:
    bonus = 100
else: bonus = 200
print(lastName,",", firstName, sep='')
print("Bonus is $", bonus, sep='')
