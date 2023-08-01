#Write a program in Python to check whether the last digit of a number is divided by 3 or not
num = int(input("Enter a Number"))
last_digit = num%10
print("last digit = ",last_digit )
if last_digit%3==0:
    print(last_digit,"is divisible by 3")
if last_digit%3!=0:
    print(last_digit,"is not divisible by 3")
