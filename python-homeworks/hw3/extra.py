#hw3 rec exercises

#4.17,
message='The secret of this message is that it\'s secret.'
length=len(message)
count=message.count('secret')
censored=message.replace('secret','xxxxxx')

#4.18
s='''
It was the best of times,
it was the worst of times;
it was the age of wisdom,
it was the age of foolishness;
it was the epoch of belief,
it was the epoch of incredulity;
it was ...
'''

def strip():
    sNew=""
    for char in range(len(s)-1):
        #for i in char:
        if s[char] not in ',.;\n':
            sNew+=s[char].lower()
        elif s[char] in ',.;':
            sNew+=' '
        #for i in range(len(s)-1):
    sNew=sNew.replace('was','is')
            
    print (sNew.strip())
    print(sNew.count('it is'))

    listS=sNew.split()
    return listS



   


    

#4.19,
def title():
    first='Marlena'
    last='Sigel'
    middle='Mae'
    print(last +',',first,middle)
    print (last+',',first, middle[0]+'.')
    print(first, middle[0]+'.',last)
    print(last+',',first[0]+'.')
    
# 4.20.
def email():
    sender='tim@abc.com'
    recipient='tom@xyz.com'
    subject='Hello!'
    print('From:',sender,'\nTo:',recipient, '\nSubject:', subject)



















