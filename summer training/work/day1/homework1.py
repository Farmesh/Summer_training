
# compute your income tax
tax_rate = 5
standard_deduction = 2000
each_dependent = 5
gross_income = int(input("enter your gross income"))
dependent = int(input("enter the dependent "))
net_income = gross_income-standard_deduction-(each_dependent + dependent)
income_tax = (net_income/gross_income)*100
print(income_tax)