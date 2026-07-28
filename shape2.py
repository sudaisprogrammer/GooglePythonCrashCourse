def lefttriangle(rows):
    space = rows
    for i in range(rows+1):
        for j in range(space-i):
            print(" ",end=" ")
        for k in range(i):
            print("*",end=" ")
        print(" ")

lefttriangle(4)