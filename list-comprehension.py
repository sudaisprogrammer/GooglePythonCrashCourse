#list comprehension in python

#what is list comprehension?
#list comprehension is a concise way to create lists in python. It consists of brackets containing an expression followed by a for #clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists. 

#list comprehension is more compact and faster than normal functions and loops for creating list.

numbers = [1, 2, 3, 4, 5]

cubes = [y*y*y for y in range(1,len(numbers)+1)]
print(cubes)


#sum of each index in list

sum = [x+x for x in range(1,6)]
print(sum)

#even numbers

nums = [1,2,3,34,56,7,78,89,45,23,1,2,67,8,67,77]

even = [x for x in nums if x%2==0]
print(even)

#multiples of 4

# multiples = [x for x in range(1,100)  if x%7==0]
multiples = [x*7 for x in range(1,10)]
print(multiples)

