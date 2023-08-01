num = int(input("enter a positive number"))
b = num
a = 0
sum = 0
while(num>0):
    a = num%10
    sum += a
    num//=10

print("sum of all digits of",b,"is =",sum )
