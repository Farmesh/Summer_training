 # palidrome - number = its reverse
num = int(input("enter a number"))
b = num
rev = 0
while(b>0):
    a = b%10
    rev = rev*10+a
    b//=10

if(rev == num):
    print(num,"is Palidrome Since",num,"=",rev)
else:
     print(num,"is not a Palidrome Since",num," != ",rev)