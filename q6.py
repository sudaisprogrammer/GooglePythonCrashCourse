def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.lower().split()
  k = 0
  for word in words:
        i = len(words[k])
        words[0:1] = words[i]
        print(words[k])
        k+=1
        
 
    # Create the pig latin word and add it to the list
    
#     if word.endswith(" "):
#       say.append()
#     # Turn the list back into a phrase
#   return 
    
# print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
# print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

pig_latin("iam am sudais ahmad")