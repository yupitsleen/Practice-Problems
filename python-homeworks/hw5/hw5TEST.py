# hw5TEST.py

>>> from hw5 import *

##### leap #####


>>> leap(2008)
True
>>> leap(1900)
False
>>> leap(2000)
True
>>> leap(2008)==True
True
>>> [ (y,leap(y)) for y in range(1900,2100,7)]
[(1900, False), (1907, False), (1914, False), (1921, False), (1928, True), (1935, False), (1942, False), (1949, False), (1956, True), (1963, False), (1970, False), (1977, False), (1984, True), (1991, False), (1998, False), (2005, False), (2012, True), (2019, False), (2026, False), (2033, False), (2040, True), (2047, False), (2054, False), (2061, False), (2068, True), (2075, False), (2082, False), (2089, False), (2096, True)]
>>> 

##### geometric #####

>>> geometric( [2,4,8,16,32,64,128,256])
True
>>> geometric( [2,4,6,8])
False
>>> geometric( [2,4,8,16,32,64,128,256])==True
True
>>> geometric( [2,4,6,8])==False
True


##### statement ######

>>> statement( [30.95, -15.67, 45.56, -55.0, 43.78] )
[120.29, -70.67]
>>> statement( [3.20, 4.57, -23.45, 67.12, 99.12, 0.00] )
[174.01, -23.45]
>>> statement( [30.95, -15.67, 45.56, -55.0, 43.78] )==[120.29, -70.67]  # return not print
True
>>> import random
>>> random.seed(0)
>>> [ statement([ random.uniform(-100,100) for i in range(100) ]) for i in range(10)] == [[3200.6100313991515, -1487.1479737344016], [2055.755390254062, -2957.2378355989345], [2446.3247843463596, -2525.3478106086895], [2805.288300939775, -2420.256988957914], [2748.0682038739446, -2495.145836269766], [2316.7531838904324, -3017.837370916358], [1892.0686643315566, -2774.0357042356927], [2254.9545373565857, -2751.374962203826], [2290.3737756944784, -2448.665122997929], [2691.7725430447376, -2550.7236495573998]] 
True


##### pixels #####


>>> pixels( [ [0,156,0,0], [34,0,0,0],[23,123,0,34]])
5
>>> pixels( [ [0,156,0,0], [34,0,0,0],[23,123,0,34]])==5
True
>>> pixels( [ [123,56,255], [34,0,0], [23,123,0], [3,0,0] ])
7
>>> pixels( [ [123,56,255], [34,0,0], [23,123,0], [3,0,0] ])==7
True
>>> pixels( [ [0,0], [0,0], [0,0] ]) == 0
True

##### prime #####
>>> prime(2)
True
>>> prime(17)
True
>>> prime(21)
False
>>> prime(2)==True
True
>>> prime(17)==True
True
>>> prime(21)==False
True
>>> 
>>> [ (n,prime(n)) for n in range(100,20000,777)]
[(100, False), (877, True), (1654, False), (2431, False), (3208, False), (3985, False), (4762, False), (5539, False), (6316, False), (7093, False), (7870, False), (8647, True), (9424, False), (10201, False), (10978, False), (11755, False), (12532, False), (13309, True), (14086, False), (14863, False), (15640, False), (16417, True), (17194, False), (17971, True), (18748, False), (19525, False)]
>>> 


























