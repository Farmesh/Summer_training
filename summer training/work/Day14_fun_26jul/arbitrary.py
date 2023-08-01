#*args
def fun(*kids):
    print("the youngrst child is" ,kids[2])

fun("rakesh","rahul","book")

#keyword arguments
def fun(fname,lname):
    print(fname,lname)
fun(fname="ram",lname="Kumar")

#kwars --arbitary keyword argument
def fun(*kids):
    print("the youngrst child is" ,kids["lname"])

fun(fname ="rakesh",lname="rahul",mname = "book")

#default parameter
def fun(country = "india"):
    print(country)
fun("spain")