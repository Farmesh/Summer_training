#Write a program to print the Fibonacci series up to a given number using a while loop.
num = int(input("enter a number"))
first_number = 0 
second_num = 1
i = 0
if num <= 0:
   print("Please enter a positive integer")
elif num == 1:
   print("Fibonacci sequence upto",num,":",first_number)
else:
   print("Fibonacci sequence upto :",num,"terms")
   while i < num:
       print(first_number)
       next= first_number + second_num
       first_number = second_num
       second_num = next
       i += 1
