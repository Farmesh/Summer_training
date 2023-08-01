number =int(input("enter a number "))
factorial = 1
if(number>=0):
    if(number==0 or number == 1):
         factorial = 1
    else:
          while(number>=2):
             factorial*= number
             number=number-1
    
    print("factorial of  number is ",factorial)
else:
    print("imaginary")



