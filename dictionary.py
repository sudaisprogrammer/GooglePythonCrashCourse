#dictionary in python

x = {}
print(type(x))

file_count = {"jpg":10,"cpp":12,"java":33,"csv":10}

print(file_count)

#check if jpg in file_count

print("jpg" in file_count)
print("py" in file_count)

#update value of key

file_count["jpg"] = 19
print(file_count)

#iterate key value

for key,value in file_count.items():
    print(key,value)


#printing just values

for value in file_count.values():
    print(value)

#printing just keys
for key in file_count.keys():
    print(key)


