#hw2.py
#Eileen Connor
#help from internet finding distance formula,
#and help from stack overflow for the concept of( distance>r1+r2 ) 


#3.23(f)
 
def forLoops():
    for numbers in range(5,22,4):
        print (numbers)
          
    
    
        
#3.34

def pay(hourlyWage,numHours):
    #willcompute employee's pay for the last week
    if numHours <= 40:
        return hourlyWage*numHours
    else:
        return ((numHours-40)*hourlyWage*1.5)+(hourlyWage*40)

#3.38

def abbreviation(day):
   return day[:2]


#3.39
import math
def collision(x1,y1,r1,x2,y2,r2):
    distance= math.sqrt((x2-x1)**2+(y2-y1)**2)
    if distance > r1+r2:
        return False
    else:
        return True
    
#3.40

def partition(names):
    
    for name in names:
        if name[0] in 'ABCDEFGHIJKLM':
            print (name)
        

#3.41

def lastF(FirstName,LastName):
    return LastName + ', ' + FirstName[0] + '.'



if __name__=='__main__':

   import doctest
   print( doctest.testfile('hw2TEST.py'))



#=== RESTART: C:/Users/yupit/OneDrive/Documents/Intro to programming/hw2.py ===
#TestResults(failed=0, attempted=20)
