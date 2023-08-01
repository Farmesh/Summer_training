#write a program to print greatest number between 4 digits using if if-else statement
a = int(input("enter 1st no.")) 
b = int(input("enter2nd no.")) 
c = int(input("enter 3rd no."))
d = int(input("enter 4th no.")) 
if a>b and a>c and a>d:
    print(a," is greatest no. in",a,b,c,d)
if b>a and b>c and b>d:
    print(b," is greatest no. in",a,b,c,d)
if c>b and c>a and c>d:
    print(c," is greatest number in", a,b,c,d)
if d>a and d>c and d>b:
    print(d,"is greatest number in", a ,b ,c ,d)
