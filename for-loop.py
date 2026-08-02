for x in range(10):
    print(x)

friends = ['taylor','alex','john','mia']

for friend in friends:
    print("Hi",str(friend))

values = [1,2,3,4,5,6,7,8,9,10]

sum = 0

for value in values:
    sum+=value

print("Sum is ",sum)
average = sum/len(values)
print("average is ",average)



#more about loop
product  = 1
for y in range(1,15): #two parameters
    product*=y
print(product)

#more advance about loop

step = 2
for z in range(1,20,step): #jump of step every time
    print("step is ",z)

for x in range(2,10,3):
    print(x+2)


