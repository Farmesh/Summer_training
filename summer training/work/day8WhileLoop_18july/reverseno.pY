num = int(input("enter a number"))
a = 0
b = num
rev =0
while(num>0):
    a = num%10
    rev = rev*10+a
    num//=10
print("reverse of number",b, "is =", rev)