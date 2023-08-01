#no of odd and even
count_even =0
count_odd = 0
for x in range(1,101):
    if(x%2==0):
        count_even+=1
    else:
        count_odd+=1
print("no. of even number =",count_even)
print("no. of odd number =",count_odd)