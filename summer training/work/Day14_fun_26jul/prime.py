
def prime(n):
 for number in range(2,n+1):
    if number>1:
        for i in range(2,number):
            if(number%i==0):
                break
        else:
            print(number)

def evenprime(n):
 list =[]
 list2 =[]
 for number in range(2,n+1):
    if number>1:
        for i in range(2,number):
            if(number%i==0):
                break
        else:
             list.append(number)
 for x in range(0,len(list)-1):
     if list[x]%2==0:
       list2.append(list[x])
       print("even prime numbers",list[x])

a = int(input("enter last value"))
prime(a)
#even Prime
print("even prime numbers")
b = int(input("enter a number (last)"))
evenprime(b)