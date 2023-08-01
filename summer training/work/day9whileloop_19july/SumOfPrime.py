num =10
sum = 0
i = 2
while(i<=num): #2<=100  true
    prime = True
    j =2
    while(j<i+1): #2<100
        if(i%j == 0): #100%2 == 0 true
            prime = False
            break
        j+=1
    if(prime):
        sum = sum + i 
        i = i+1

print("Sum =",sum)

