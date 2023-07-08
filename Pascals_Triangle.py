#Drawing a Pascals Triangle

def drawPascal(num):
    row = 1
    l1 = [None]*num #number of rows.
    while row <= num:
        l2 = [None]*row #number of element in each row.
        element = 0
        element = row
        while -element<0:
            if -element == -row:
                l2[-element]=1
                print(l2[-element], end = " ")
            elif -element == -1:
                l2[-element]=1
                print(l2[-element], end = " ")
                break
            else:
                l2[-element] = l1[-row+1][-element] + l1[-row+1][-element+1]
                print(l2[-element], end = " ")
            element = element-1
        
        print("")
        l1[-row] = l2
        row = row+1

rows = int(input("How Many No. of rows do you want in Pascals Triangle?:\n"))
drawPascal(rows)