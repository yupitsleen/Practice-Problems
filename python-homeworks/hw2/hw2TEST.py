# hw2TEST.py

>>> from hw2 import *

##### forLoops #####

>>> forLoops()
5
9
13
17
21
>>> 

##### pay ######

>>> pay(10,10)==100
True
>>> pay(10,35)==350
True
>>> pay(10,45)==475.00
True
>>> pay(13.25,40)==530.0
True

##### abbreviation ######


>>> abbreviation('Tuesday')
'Tu'
>>> abbreviation( 'Monday' )=='Mo'
True
>>> abbreviation( 'Wednesday' )=='We'
True

>>> abbreviation( 'Sunday' )=='Su'
True

##### collision ######


>>> collision(0,0,3,0,5,3)
True
>>> collision(0,0,1.4,2,2,1.4)
False
>>> collision(0,0,2,5,0,3)
True
>>> [collision(0,0,3,0,5,3), collision(0,0,1.4,2,2,1.4), collision(0,0,2,5,0,3)]  # return not print
[True, False, True]

##### partition ######

>>> partition(['Eleanor','Evelyn','Sammy','Owen','Gavin'])
Eleanor
Evelyn
Gavin
>>> partition(['Xena','Sammy','Owen'])
>>> partition(['April','Margaret','Frances','Jill'])
April
Margaret
Frances
Jill

##### lastF ######



>>> lastF('George','Washington')=='Washington, G.'
True
>>> lastF('Albert','Camus')=='Camus, A.'
True
>>> lastF('Hilary','Clinton')=='Clinton, H.'
True
