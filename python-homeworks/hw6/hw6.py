#hw6
#Eileen Connor


import random
import math
#5.38 done
def collatz(someInt):
    num=abs(someInt)
    print(num)
    while num>1:
        if num%2==0:
            num=num/2
            print (int(num))
        else:
            num=(3*num)+1
            print (int(num))
            
'''#5.38 recursive done
def collatz2(someInt):
    num=abs(someInt)
    
    if (num==1):
        print(num)
        return
    elif num%2==0:
        num=num/2
    else:
        num=(3*num)+1

    print (int(num))
    collatz(num)'''

#5.42 done
def primeFac(intN):
    num=intN
    nFac=[]
    for i in range(2,num+1):
        while num !=1:
            if num%i==0:
                num=num/i #invariant
                nFac.append(i)
            else:
                break
    return nFac

#5.48 done
def sublist(list1, list2):
    startAt=0
    sublist1=[]
    for i in range(len(list1)):
        if startAt==len(list2):
            break
        for j in range(startAt,len(list2)):
            if list1[i]==list2[j]:
                startAt=j+1
                sublist1.append(list1[i])
                break
            else:
                continue
    return sublist1==list1
    
    #'cross out' irrelevant items in second list-->hint
            #i and j counters
            #while you still have numbers in both lists
            #i=j mean increment both
            #no match means increment just j
            #if first list exhausted, then True
            #do not use sets
            #similiar to previous problem stategy
            #try printing or printing vars()
            

#6.22 done
def mirror(word):
    letterDict={'q':'p', 'p':'q','d':'b','b':'d'}
    newWord=''
    for letter in word:
        if letter not in 'qwtuiopdlxvbnmWTYUIOAHXVM':
            return 'INVALID'
    for i in range(len(word)):
        if word[i] in letterDict:
            newWord+=letterDict[word[i]]
        else:
            newWord+=word[i]
    return newWord[::-1]
            
    
            
#6.30 done
def rps():
    poss=['R','P','S']
    player1=random.choice(poss)
    player2=random.choice(poss)
    ans=str(player1+player2)
    if ans=='RS' or ans=='SP' or ans=='PR':
        return -1
    elif ans=='SR' or ans=='PS' or ans=='RP':
        return 1
    else:
        return 0
    
def simul(intN):
    rounds=intN
    player1Win=0
    player2Win=0
    ties=0
    numGames=0
    while numGames<=rounds:
        numGames+=1
        winner=rps()
        if winner==-1:
            player1Win+=1
        elif winner==1:
            player2Win+=1
        else:
            ties+=1
    if player1Win>player2Win:
        print('Player 1')
    elif player2Win>player1Win:
        print ('Player 2')
    else:
        print ('Tie')

#6.31 done
'''def craps2():
    import random
    di1=random.randrange(1,7)
    di2=random.randrange(1,7)
    dice=di1+di2
    if dice==7 or dice==11:
        return 1
    elif dice==2 or dice==3 or dice==12:
        return 0
    else:
        di3=random.randrange(1,7)
        di4=random.randrange(1,7)
        dice2=di3+di4
        while dice2!=dice and dice2!=7:
            if dice2==7:
                return 1
            elif dice2==dice:
                return 0
            else:
                break'''
            
def craps():
    roll = random.randrange(1,7) + random.randrange(1,7)
    if roll==7 or roll==11:
        return 1
    elif roll==2 or roll==3 or roll==12:
        return 0
    else:
        newRoll=random.randrange(1,7) + random.randrange(1,7)
        while newRoll!=roll and newRoll!=7:
            newRoll = random.randrange(1,7) + random.randrange(1,7)

        return int(newRoll == roll)


def testCraps(someInt):
    n=abs(someInt)
    wins=0
    total=0
    while total<=n:
        wins+=craps()
        total+=1
    return wins/total
            



if __name__=='__main__':

   import doctest
   print( doctest.testfile('hw6TEST.py'))
