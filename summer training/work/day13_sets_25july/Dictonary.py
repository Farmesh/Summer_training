dictionary = {"name":"ram","age":25}
print(dictionary)

x= dictionary.keys()  #fetch keys
print("keys =",x)

y = dictionary.values()  #fetch values
print("values =",y)

z = dictionary.items()
print("items =",z)

#searching
if "name" in dictionary:
    print("YES")
else:
    print("NO")

#add data
dictionary["mobileno"]=7876602243
print(dictionary)

#2nd method ---update method
dictionary.update({"college":"IITB"})
print(dictionary)


#removing data

dictionary.pop("age")
print(dictionary)


#looping

for x in dictionary:
    print(x)

for x in dictionary.values():
    print(x)

for x in dictionary.items():
    print(x)
