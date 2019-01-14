#hw8
#Eileen Connor

##1
class Pizza:
    def __init__(self, size='M', toppings=None):
        self.s=size
        if toppings is None:
            toppings = set() #done bc sets are immutable
        self.t=toppings
    def __repr__(self):
        return 'Pizza(\'{}\',{})'.format(self.s,self.t)
    def __eq__(self,other):
        return (self.s,self.t)==(other.s,other.t)
    def setSize(self,size):
        if size in 'SML':
            self.s=size.upper()
        else:
            self.s='M'
    def getSize(self):
        return self.s
    def addTopping(self,topping):
        self.t.add(topping)
    def removeTopping(self,topping):
        self.t.remove(topping)
    def price(self,price=0.0):
        if self.s=='S':
            price=6.25
            for topping in self.t:
                price+=0.7
        elif self.s=='M':
            price=9.95
            for topping in self.t:
                price+=1.45
        else:
            price=12.95
            for topping in self.t:
                price+=1.85
        return price

##2
def orderPizza():
    
    myPizza = Pizza()

    print('Welcome to Python Pizza!')
    size=input('What size pizza would you like (S,M,L): ')
    myPizza.setSize(size)

    topping=input('Type topping to add (or Enter to quit): ')
    while topping !='':
        myPizza.addTopping(topping)
        topping=input('Type topping to add (or Enter to quit): ')
        
    print ('Thanks for ordering!')
    print ('Your pizza costs ${}'.format(myPizza.price()))
    return myPizza



####3
class Stack(list):
    #LIFO
#sub/child class of the super/parent class
#pop and len already inherited
#must define push: single item
#must write repr
#be careful for infinite recursion
#inheritance needs diff repr:
    
    def __repr__(self):
        return 'Stack({})'.format(list.__repr__(self))
           #called extending a method. could also do list(self) but not as good
    def push(self,item):
        self.append(item)
    def isEmpty(self):
        return self==[]
    
####4
def parenthesesMatch(string):
    #dont need to index...compare the popped item
        #to closing par w/ iteration
           #check beginning first or
        #else dont do
    #[{},[]...]
    opp = {'{':'}','[':']','(':')'}
    for bracket in string:
        if bracket not in '[]{}()':
            return False
        else:
            continue
    stack=[]
    for bracket in string:
        if bracket in '[{(':
            stack.append(bracket)
            
        elif bracket in ']})' and stack==[]:
            return False
        elif bracket in ']})' and stack!=[]:
            openBracket = stack.pop()
            if opp[openBracket] == bracket:
                continue
            else:
                return False
          
    return stack==[]

##########

 opp = {'{':'}','[':']','(':')'}
    for bracket in string:
        if bracket not in '[]{}()':
            return False
        else:
            continue
    stack=Stack()
    for bracket in string:
        if bracket in '[{(':
            stack.push(bracket)
            
        elif bracket in ']})' and stack.isEmpty():
            return False
        elif bracket in ']})' and not stack.isEmpty():
            openBracket = stack.pop()
            if opp[openBracket] == bracket:
                continue
            else:
                return False
          
    return stack.isEmpty()

 




           
##doctest

if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw8TEST.py'))

