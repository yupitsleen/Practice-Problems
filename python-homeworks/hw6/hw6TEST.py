# hw6TEST.py

>>> from hw6 import *

##### collatz #####

>>> collatz(10)
10
5
16
8
4
2
1
>>> collatz(3)
3
10
5
16
8
4
2
1
>>> [collatz(i) for i in range(4,7)]
4
2
1
5
16
8
4
2
1
6
3
10
5
16
8
4
2
1
[None, None, None]
>>> 


##### primeFac #####

>>> primeFac(5)
[5]
>>> primeFac(72)
[2, 2, 2, 3, 3]
>>> primeFac(72)==[2, 2, 2, 3, 3]
True
>>> [ (i,primeFac(i)) for i in range(10,300,23)]
[(10, [2, 5]), (33, [3, 11]), (56, [2, 2, 2, 7]), (79, [79]), (102, [2, 3, 17]), (125, [5, 5, 5]), (148, [2, 2, 37]), (171, [3, 3, 19]), (194, [2, 97]), (217, [7, 31]), (240, [2, 2, 2, 2, 3, 5]), (263, [263]), (286, [2, 11, 13])]


##### subList #####


>>> sublist([15,1,100],[20,15,30,50,1,100])==True
True
>>> sublist([15,50,20],[20,15,30,50,1,100])==False
True
>>> sublist([1,1,1,2,2,2],[1,1,1,2,2])==False
True
>>> sublist([1,2],[2,2,2,5,5,5,1,1,1])==False
True
>>> sublist( [1,2,2,3],[1,1,2,2,3])
True

##### mirror #####

>>> mirror('vow')
'wov'
>>> mirror('wood')
'boow'
>>> mirror('bed')
'INVALID'
>>> mirror(mirror('vow'))
'vow'
>>> 


##### simul #####

>>> import random
>>> random.seed(0)
>>> simul(1)
Tie
>>> random.seed(0)
>>> simul(100)
Player 1
>>> random.seed(1)
>>> simul(100)
Player 2
>>> [ (i, random.seed(i), simul(10*i)) for i in range(1,10)]
Player 1
Player 1
Player 2
Player 2
Player 2
Player 1
Player 1
Player 2
Player 2
[(1, None, None), (2, None, None), (3, None, None), (4, None, None), (5, None, None), (6, None, None), (7, None, None), (8, None, None), (9, None, None)]
>>> 


##### craps #####

>>> import random
>>> random.seed(0)
>>> craps()
0
>>> random.seed(1)
>>> craps()
1
>>> random.seed(2)
>>> craps()
0
>>> [ (i,random.seed(i),craps()) for i in range(20)]
[(0, None, 0), (1, None, 1), (2, None, 0), (3, None, 1), (4, None, 0), (5, None, 1), (6, None, 0), (7, None, 1), (8, None, 0), (9, None, 0), (10, None, 1), (11, None, 1), (12, None, 1), (13, None, 1), (14, None, 0), (15, None, 0), (16, None, 1), (17, None, 0), (18, None, 0), (19, None, 1)]
>>> 

##### testCraps #####

>>> random.seed(0)
>>> testCraps(10000)
0.5
>>> random.seed(1)
>>> testCraps(10000)
0.4921
>>> [(i,random.seed(i),testCraps(100*i)) for i in range(1,10)]
[(1, None, 0.49), (2, None, 0.46), (3, None, 0.47333333333333333), (4, None, 0.5125), (5, None, 0.476), (6, None, 0.47333333333333333), (7, None, 0.4514285714285714), (8, None, 0.48), (9, None, 0.4855555555555556)]
>>> 











