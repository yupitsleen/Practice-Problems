def classComparison():
    oldLst= open('AV Roster FQ18.csv' ).read()
    lastName=[]
    firstName=[]
    oldRows=oldLst.split('\n')
    for row in oldRows[:-1]:
        columns=row.split(',')
        lastName.append(columns[4])
        firstName.append(columns[5])

    newLst= open('FQ18 AV Roster 2.csv').read()
    lastName2=[]
    firstName2=[]
    newRows=newLst.split('\n')
    for row2 in newRows[:-1]:
        columns2=row2.split(',')
        lastName2.append(columns2[1])
        firstName2.append(columns2[2])

    for lname in lastName:
        if lname not in lastName2:
            print(lname)

    print('_____________\n')

    #for fname in firstName:
     #   if fname not in firstName2:
           # print(fname)
            

classComparison()
