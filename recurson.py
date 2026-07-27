def factorial(n):
    if n ==1: #base case very very very important
        return 1
    return n*factorial(n-1) #function is calling itself

print(factorial(5))