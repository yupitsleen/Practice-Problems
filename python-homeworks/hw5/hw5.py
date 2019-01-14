#hw5
#Eileen Connor

#5.25 
def leap(year):
    if year %4==0 and (year %100!=0 or year %400==0):
       return True
    return False

#5.28 
def geometric(intLst):
    ratios=[]
    for i in range(len(intLst)-1):
        ratios.append(intLst[i+1]/intLst[i])
    for i in range(len(ratios)-1):
        if ratios[i] != ratios[i+1]:
            return False
    return True
#5.34 
def statement(floatLst):
    deposits=0
    withdrawls=0
    for num in floatLst:
        if num>0:
            deposits+=num
        elif num<0:
            withdrawls+=num
    total=[deposits,withdrawls]
    return total
#5.35 
def pixels(lstLst):
    count=0
    for lst in lstLst:
        for num in lst:
            if num>0:
                count+=1
    return count
#5.36
def prime(num):
    count=0
    for i in range(num+1):
        if i>=1:
            if num%i==0:
                count+=1
    if count>2:
        return False
    return True
    


if __name__=='__main__':

   import doctest
   print( doctest.testfile('hw5TEST.py'))
