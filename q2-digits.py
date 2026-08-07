def digits(num):
    count = 0
    n = num
    # if num == 0:
    #     count+=1
    while (n!=0):
        num = n%10
        n = n//10
        count+=1
    return count

n = digits(3411)
print(n)

