
# Solutions to recommended problems 4.17, 4.18, 4.19, and 4.20 here:

"""
#4.17

>>> message = "The secret of this message is that it is secret."
>>> length = len( message )
>>> count = message.count("secret")
>>> censored = message.replace("secret","xxxxxx")
>>> censored
'The xxxxxx of this message is that it is xxxxxx.'

#4.18

>>> s = '''It the best of times, it was the worst of times; it
was the age of wisdom, it was the age of foolishness; it was the
epoch of belief, it was the epoch of incredulity; it was ...'''
>>> table = str.maketrans(".,;\n",4*' ')
>>> newS = s.translate(table)
>>> newS = newS.strip()
>>> newS = newS.lower()
>>> newS.count("it was")
6
>>> newS = newS.replace("was","is")
>>> listS = newS.split()


#4.19

>>> print(last + ",", first, middle)
Sigel, Marlena Mae
>>> print(last + ",", first, middle[0]+'.')
Sigel, Marlena M.
>>> print(first,middle[0]+'.',last)
Marlena M. Sigel
>>> print(first[0]+'.',middle[0]+'.',last)
M. M. Sigel

#4.20

>>> print("From:",sender,"\nTo:",recipient,"\nSubject:",subject)
From: tim@abc.com 
To: tom@xyz.org 
Subject: Hello!

"""
