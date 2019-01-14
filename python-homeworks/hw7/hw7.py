#hw7
#Eileen Connor

#####1
class Volume:
    #stereo volume b/w 0 and 11
    def __init__(self, initialLvl=0):
        self.set(initialLvl)
        
    #gaurantees that every volume gets a new value
        
    def __repr__(self):
        return 'Volume({})'.format(self.level)

    def __eq__(self,other):
        return self.level==other.level
    #returns True if Volumes have the same value
    
    def get(self):
        return self.level

    def set(self, vol):
        if vol<0:
            self.level=0
        elif vol>11:
            self.level=11
        else:
            self.level=vol

    def up(self, moveUpBy):
        self.set(self.level+moveUpBy)

    def down(self, moveDownBy):
        self.set(self.level-moveDownBy)

############2
def partyVolume(fileStr):

    myFile=open(fileStr)
    initValue=eval(myFile.readline())
    myVol=Volume(initValue)
    restV=myFile.readlines()
    myFile.close()
    
    for line in restV:
        line=line.strip('\n').split(' ')
        if line[0]=='U':
            myVol.up(eval(line[1]))
        elif line[0]=='D':
            myVol.down(eval(line[1]))
            
    return myVol






if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'hw7TEST.py'))
