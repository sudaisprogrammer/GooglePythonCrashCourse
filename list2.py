#methods of list

score = [3,45,77,12,56,11,90,76,31,33,41]
laptop = ["dell","hp","lenovo","asus","acer","samsung","apple","microsoft"]

score.append(120) #append method is used to add an element at the end of the list
print(score)

newscore = [120,333,411]

score.extend(newscore) #extend method is used to add multiple elements at the end of the list
print(score)

score.insert(3,10000) #insert method is used to add an element at a specific index
print(score)


score.pop(2) #pop method is used to remove the specified index default is last element of the list
print(score)

score.sort(reverse=False) #sort method is used to sort the list in ascending order
print(score)

score.reverse() #reverse method is used to reverse the list
print(score)

# score.count(11) #count method is used to count the number of occurrences of an element in the list
print(score.count(11))