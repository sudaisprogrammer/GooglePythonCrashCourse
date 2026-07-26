#functions are the building blocks of any programming langauge
#like a car has a engine to function well to start the car and so on there are multiple functions which are nescessary to operate a car

#in python there are two types of functions like builtin functions and user defined fucntions
#here we will explore both of these
#in python user defined function are built using def keyword

def saygreet(name):
    print("Good Morning! "+name)

saygreet("Ahmad") #function call without this the function can'nt be invoked

#the above function take one paramter as string and give the desired output

def add1(a,b):
    return a+b #here we are returning values to our called function variable

sum = add1(1,2)
print("Sum is ",sum)

def area_triangle(base,height):
    return (1/2)*(base*height)

print("area of triangle is ",area_triangle(2,3))