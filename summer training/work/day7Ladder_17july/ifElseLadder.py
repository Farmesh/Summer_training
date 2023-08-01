
sub1 = int(input("enter marks in sub 1"))
sub2 = int(input("enter marks in sub 2"))
sub3 =int(input("enter marks in sub 3"))
sub4 = int(input("enter marks in sub 4"))
sub5 = int(input("enter marks in sub 5"))

total =sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total/500)*100
print("total marks = ",total)

print("Percentage = ",percentage)

if(percentage>=45 and percentage<=60):
    print("D grade")

elif(percentage>=60 and percentage<=75):
    print("C grade")

elif(percentage>=75 and percentage<=85):
    print("B grade")

elif(percentage>=85 and percentage<=100):
    print("A grade")
elif( percentage<45):
    print("Fail")
else:
    print("Error")

