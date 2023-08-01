
angle1 = int(input("enter  angle 1"))
angle2 = int(input("enter  angle 2"))
angle3 =int(input("enter  angle 3"))
sum =angle1+angle2+angle3
if((angle1<90 and angle2<90 and angle3<90)and sum<=180):
    print("acute angled triangle")
elif((angle1==90 or angle2==90 or angle3==90) and sum<=180):
    print("Right angled Triangle")
elif((angle1>90 or angle2>90 or angle3>90 )and sum<=180):
    print("Obtuse")
else:
    print("Triangle Not exist")
