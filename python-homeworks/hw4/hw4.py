#hw4
#Eileen Connor

#5.15 DONE
def vowels(someStr):
    for i in range(len(someStr)):
        if someStr[i] in 'aeiouAEIOU':
            print (i)
        
    
#5.16 DONE
def indexes(word, char):
    lst=[]
    
    for i in range(len(word)):
        if word[i] == char:
            lst.append(i)
    return lst
        
    

#5.18 DONE
def four_letter(wrdLst):
    fourLetters=[]
    for word in wrdLst:
        if len(word)==4:
            fourLetters.append(word)
    return fourLetters
    
#5.26 DONE
def rps(playerOne, playerTwo):
    ans=str(playerOne+playerTwo).upper()
    
    if ans=='RS' or ans=='SP' or ans=='PR':
        return -1
    elif ans=='SR' or ans=='PS' or ans=='RP':
        return 1
    else:
        return 0
    
    
#5.39 DONE
def exclamation(someStr):
    newLst=""
    
    for vowel in someStr:
        if vowel in "aeiouAEIOU":
            for i in range(4):
                newLst+=vowel
        else:
            newLst+=vowel
    return newLst+'!'

        
            
    
        
            
            


if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw4TEST.py'))



