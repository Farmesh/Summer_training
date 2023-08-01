a =[]
even =[]
odd=[]
count_odd = 0
count_even = 0 
total = int(input("enter total number of values in list"))
for i in range(total):
    print("enter",i+1,"th","value")
    inpt = int(input())
    a.append(inpt)
for i in range(total):
    value = a[i]
    if(value%2==0):
        count_even = count_even+1
        even.append(a[i])
    else:
        count_odd = count_odd+1
        odd.append(a[i])

print("odd list =",odd)
print("odd count = ",count_odd)
print("even List =", even)
print("even count = ",count_even)