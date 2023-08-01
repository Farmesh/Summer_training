a =int(input("enter a number of rows"))


for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
print()
for i in range(0,a+1):
    for j in range(1,i+1):
        print(i,end="")
    print()
print()

for i in range(1,a+1):
    for k in range(a,i,-1):
             print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
print()
for i in range(1,a):
    for j in range(i,a):
         print(" ",end = "")
    for k in range(0,((2*i)-1)):
          print("*",end="")
    print()
print()
for i in range(0,a):
    for j in range(0,a):
          print("*",end=" ")
    print()
print()

for i in range(1,a+1):
    for j in range(i,a):
         print(" ",end = "")
    for k in range(0,((2*i)-1)):
          print("*",end="")
    print()
for i in range(1,a):
    for j in range(0,i):
         print(" ",end = "")
    b = 2*a -(2*i+1)
    for k in range(1,b+1):
          print("*",end="")
  
    print()
print()

for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end="")
    b = 2*a -(2*i+1)
    for k in range(1,b+1):
          print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*",end="")
    b = 2*a -(2*i+1)
    for k in range(1,b+1):
          print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
   
  
    print()
    print()