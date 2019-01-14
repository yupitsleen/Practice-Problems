#hw3
#Eileen Connor

 #4.24
def cheer(team):
    s="How do you spell winner?\nI know, I know!\n"
    for char in team:
        s+=char.upper() + " "

    s+="!\nAnd that's how you spell winner!" +"\nGo " + team + '!'
    print(s)          

 #4.25
def vowelCount(phrase):
    #countLst indexed as a,e,i,o,u
    countLst=[0,0,0,0,0]
    #vowels=""
    for char in phrase:
        if char.lower() == "a":
            countLst[0]+=1
        elif char.lower()=="e":
            countLst[1]+=1
        elif char.lower()=="i":
            countLst[2]+=1
        elif char.lower()=="o":
            countLst[3]+=1
        elif char.lower()=="u":
            countLst[4]+=1
    print("a, e, i, o, and u appear, respectively, " + str(countLst).strip('[]') + " times.")
           
 #4.26
def crypto(someFile):
    file=open(someFile)
    print(file.read().replace('secret','xxxxxx'))
    file.close()
                
 #4.28
def links(webFile):
    infile=open(webFile,'r')
    fileTxt=infile.read()
    infile.close()
    #print(fileTxt)
    return fileTxt.count("</a>")
    #for link in fileTxt:
        #print (link.count("</a>"))
        
 #4.31
def duplicate(fileName):
    openFile=open(fileName)
    fileTxt=openFile.read()
    openFile.close()
    txtLst=fileTxt.split(" ")
    for word in txtLst:
        if txtLst.count(word)>1 :
            return True
    return False



if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw3TEST.py'))
    
    






    


