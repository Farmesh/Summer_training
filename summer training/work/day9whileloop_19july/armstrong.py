#Write a program to check if a given number is an Armstrong number using a while loop.
num = int(input("Enter a number"))
sum = 0
a = num
while a > 0:
   digit = a % 10
   sum += digit ** 3
   a //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
