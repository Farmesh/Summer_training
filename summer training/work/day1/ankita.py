# calculate simple interest
principle = 500
rate = 5
time = 3
simple_interest = (principle*rate*time)*100
print("simple interest =")
print(simple_interest)

# calculate area of circle
radius = 20
area = (3.14*radius*radius)
print("area of circle")
print(area)

# area of square 
side = 50
area = side*side
print("area of square")
print(area)

# total and percentage of 5 subjects
sub1 = 60
sub2 = 15
sub3 = 70
sub4 = 40
sub5 = 30
total = sub1+sub2+sub3+sub4+sub5
percentage = (total/500)*100
print("total")
print(total)
print("percentage")
print(percentage)

# dollar to rupees
number = int(input("enter a value in dollar"))
rupees = 78*number
print("value in rupees")
print(rupees)

# volume of cylinder 
radius = int(input("enter radius"))
height = int(input("enter height"))
print("volume")
volume = 3.14*radius*radius*height
print(volume)

# compute your income tax
taxRate = 60
standardDeduction = 300
eachDependent = 2000
grossIncome = int(input("enter your gross income"))
dependent = int(input("enter the dependent "))
netIncome = grossIncome-standardDeduction-(eachDependent+dependent)
incomeTax = (netIncome/grossIncome)*100
print(incomeTax)

