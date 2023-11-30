weeklyHoursWorked=float(input("Enter weekly hours worked:"))
hourlyRate=float(input("Enter hourly rate:"))
OT_RATE=1.5
FULL_HOURS=40
if weeklyHoursWorked>40:
    weeklyGrossPay = hourlyRate * FULL_HOURS + hourlyRate * OT_RATE * (weeklyHoursWorked - FULL_HOURS)

else:
    weeklyGrossPay = hourlyRate * weeklyHoursWorked

print('Weekly gross pay $', weeklyGrossPay, sep='')
