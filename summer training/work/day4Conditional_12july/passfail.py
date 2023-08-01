#pass or fail
sub1 = int(input("enter marks in sub 1"))
sub2 = int(input("enter marks in sub 2"))
sub3 = int(input("enter marks in sub 3"))
sub4 = int(input("enter marks in sub 4"))
sub5 = int(input("enter marks in sub 5"))
percentage = ((sub1+sub2+sub3+sub4+sub5)/500)*100  #calculate percentage
if percentage>=60:
    print("Pass")
if percentage<60:
    print("fail")