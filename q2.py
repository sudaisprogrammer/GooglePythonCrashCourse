# Question 4
# Fill in the gaps in the nametag function so that it uses the format method to return first_name and the first initial of last_name followed by a period. For example, nametag("Jane", "Smith") should return "Jane S."

def nametag(first_name, last_name): #function to return first name and first initial of last name
    return("{} {}.".format(first_name,last_name[0]))


print(nametag("Jane", "Smith")) 
print(nametag("Francesco", "Rinaldi")) 
print(nametag("Jean-Luc", "Grand-Pierre")) 
