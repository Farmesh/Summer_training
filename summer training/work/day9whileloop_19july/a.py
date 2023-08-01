#Write a program to check if a given number is prime using a while loop.
number = int(input("Enter a number"))  
a = 0
i = 2
while i <= number / 2:
    if number % i == 0:
        a=1
        break
    i=i+1
    
if a==0:
    print("The entered number is a PRIME number")
else:
    print("The entered number is not a PRIME number")