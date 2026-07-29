#program to find maximum odd numbers like if num = 10 then output must be 1,3,5,7,9 and so on
def maximum_odd(num):
    return_string = ""
    for i in range(1,num):
        if i%2!=0:
            return_string +=f",{i}"
    return return_string.rstrip()


print(maximum_odd(6)) 
print(maximum_odd(12))
print(maximum_odd(123))