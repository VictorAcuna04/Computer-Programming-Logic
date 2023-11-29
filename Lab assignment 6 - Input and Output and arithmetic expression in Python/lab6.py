#set the tax rate to 0.2
TAX_RATE = 0.2
#set the standard deduction to 10000.00
STANDARD_DEDUCTION = 10000.00
#set the dependent deduction to 2000.0
DEPENDENT_DEDUCTION = 2000.0
#set the standard deduction to 10000.00
STANDARD_DEDUCTION = 10000.00
#input the gross income
grossIncome = float(input("Input gross income: "))
#input the number of dependents
dependents = float(input("Input the number of dependents: "))
#determine the dependent deduction
dependentDeduction = dependents * DEPENDENT_DEDUCTION
#determine the gross income after deduction
grossIncomeAfterDeduction = grossIncome - (dependentDeduction + STANDARD_DEDUCTION)
#determine the income tax
incomeTax = grossIncomeAfterDeduction * TAX_RATE
#determine the gross income after tax
grossIncomeAfterTax = grossIncome - incomeTax
#display the income tax
print("Income Tax: $", incomeTax, sep='')
#display the gross income after tax
print("Gross Income After Tax: $", grossIncomeAfterTax, sep='')

