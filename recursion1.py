#visualing recursion using python

def factorial(n):
    if n==1:
        print("Returning 1")
        return 1
    print("Returning ",str(n))
    return n*factorial(n-1)

print("factorial is ",factorial(8))