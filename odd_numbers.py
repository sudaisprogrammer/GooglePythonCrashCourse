def maximum_odd(num):
    return_string = ""
    for i in range(1,num):
        if num%2!=0:
            return_string +=f",{i}"
    return return_string.rstrip()


print(maximum_odd(6))