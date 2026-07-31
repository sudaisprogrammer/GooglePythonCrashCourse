sentence = "i am sudais ahmad"

name = "ahmad"
newsentecne = ""
if sentence.endswith(name):
    print("The sentence ends with the name")
    i = sentence[0:len(sentence)+len(name)]
    print(i)
else:
    print("The sentence does not end with the name")