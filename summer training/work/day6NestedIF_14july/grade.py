sub1 = 46
sub2 = 60
sub3 = 24
sub4 = 24
sub5 = 80

total =sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total/500)*100
print("total marks = ")
print(total)

print("Percentage = ")
print(percentage)

if(percentage>=50):
        if(percentage>=50 and percentage<=90):
                print(" B Grade")
        else:
                print(" A Grade")
else:
        print("You are Fail ! Surprise ")     


