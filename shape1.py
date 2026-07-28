def triangle(rows):
    for i in range(1,rows+1):
        for j in range(i):
            print(" * ",end="")
        print(" ")

triangle(5) #it will create triangle with 5 rows