name = "my laptop"

# print(name*4)

print(name[:3])
print(name[1:3])
print(name[-3:-1])
print(name[:-1]) #in python -negative indexing starts from the end of the string

#converting int into string
num = 123
print(type(num)) #here the type of num is int
num_str = str(num)
print(num_str)
print(type(num_str)) #type function is used to check the type of variable,but here the type of num_str is string


# we can also use the format function to convert int into string
book  = "let us C"
pages = 450
print("The book name is {} and it has {} pages".format(book,pages)) #curly braces are used to insert the values of book and pages into the string

#we can also use placeholders to insert the values of book and pages into the string
print("The book name is %s and it has %d pages"%(book,pages))
#another way to use placeholders is to use f-strings
print(f"The book name is {book} and it has {pages} pages")


#working with decimals

price = 49.99
with_tax = price * 1.15

print("The price of the product is ${:.2f} and with tax it is ${:.2f}".format(price,with_tax)) #here {:.2f} is used to format the float value to 2 decimal places

