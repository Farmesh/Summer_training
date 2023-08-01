print("Swapping Using three variable") 
a = int(input("enter value of a")) #12
b = int(input("enter value of b")) #98
print("Before Swapping")
print("a = " ,a ," b = ", b)
c = a #12
a = b #98
b = c #12 
print("After Swapping")
print("a = " ,a ," b = ", b)

print("Swapping Using Two variable") 

x = int(input("enter value of a"))
y = int(input("enter value of b"))
print("Before Swapping")
print("x = " ,x ," y = ", y)
x , y = y , x
print("After Swapping")
print("x = " ,x ," y = ", y)