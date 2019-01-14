# hw4TEST.py

>>> from hw4 import *

##### vowels #####

>>> vowels('Hello WORLD')
1
4
7
>>> vowels('lynx')
>>> vowels('abracadabra')
0
3
5
7
10
>>> 



##### indexes #####

>>> indexes('mississippi','s')
[2, 3, 5, 6]
>>> indexes('mississippi','i')
[1, 4, 7, 10]
>>> indexes('mississippi','a')
[]
>>> indexes('mississippi','s')==[2, 3, 5, 6]
True
>>> indexes('mississippi','i')==[1, 4, 7, 10]
True
>>> indexes('mississippi','a')==[]
True
>>> 


##### four_letter #####

>>> four_letter(['dog','letter','stop','door','bus','dust'])
['stop', 'door', 'dust']
>>> four_letter(['dog','letter','stop','door','bus','dust'])==['stop', 'door', 'dust']
True
>>> four_letter(['dog','letter'])
[]
>>> four_letter([])
[]
>>> 

##### rps #####

>>> rps('R','P')
1
>>> rps('R','S')
-1
>>> rps('S','S')
0
>>> [ (p1,p2,rps(p1,p2)) for p1 in 'RPS' for p2 in 'RPS']
[('R', 'R', 0), ('R', 'P', 1), ('R', 'S', -1), ('P', 'R', -1), ('P', 'P', 0), ('P', 'S', 1), ('S', 'R', 1), ('S', 'P', -1), ('S', 'S', 0)]
>>> 




##### exclamation #####


>>> exclamation('argh')
'aaaargh!'
>>> exclamation('hello')
'heeeelloooo!'
>>> exclamation('awesome')
'aaaaweeeesoooomeeee!'
>>> exclamation('excellent')
'eeeexceeeelleeeent!'
>>> exclamation('why')
'why!'
>>> 















