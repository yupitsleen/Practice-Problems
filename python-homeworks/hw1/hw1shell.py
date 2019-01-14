Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #hw1.py
>>> import numpy
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import numpy
ModuleNotFoundError: No module named 'numpy'
>>> x = sum(-1:-7)
SyntaxError: invalid syntax
>>> negNums=[-1, -2, -3, -4, -5, -6, -7]
>>> sum(negNums)
-28
>>> negNums=[-1, -2, -3, -4, -5, -6, -7]
sum(negNums)
-28

SyntaxError: multiple statements found while compiling a single statement
>>> campKids= [(17*9), (24*10), (21*11), (27*12)]
>>> avgAge=sum(campKids)/len(campKids)
>>> angAge
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    angAge
NameError: name 'angAge' is not defined
>>> avgAge
237.0
>>> numCampKids= [17, 24, 21, 27]
>>> avgAge=sum(campKids)/sum(numCampKids)
>>> avgAge
10.651685393258427
>>> 2^-20
-18
>>> 2**-20
9.5367431640625e-07
>>> 4356/61
71.40983606557377
>>> 4356%61
25
>>> s1='-'
>>> s2='+'
>>> s1+s2
'-+'
>>> s1+s2+s1
'-+-'
>>> s2+(s1*2)
'+--'
>>> 
>>> s2+(s1*2)+s2+(s1*2)
'+--+--'
>>> (s2+(s1*2))*2
'+--+--'
>>> s='goodbye'
>>> s==g
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s==g
NameError: name 'g' is not defined
>>> s[0]=='g'
True
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
== RESTART: C:/Users/yupit/OneDrive/Documents/Intro to programming/test2.py ==
hello world
>>> 
== RESTART: C:/Users/yupit/OneDrive/Documents/Intro to programming/test2.py ==
hello world
>>> 
== RESTART: C:/Users/yupit/OneDrive/Documents/Intro to programming/test2.py ==
hello world
>>> 
== RESTART: C:/Users/yupit/OneDrive/Documents/Intro to programming/test2.py ==
>>> 
== RESTART: C:/Users/yupit/OneDrive/Documents/Intro to programming/test3.py ==
matthew
>>> 
>>> 
>>> 
>>> 
>>> s[6]=='g'
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    s[6]=='g'
NameError: name 's' is not defined
>>> s='goodbye'
>>> s[6]=='g'
False
>>> s[0:1]=='ga'
False
>>> s[-2]=='x'
False
>>> s[3]=='d'
True
>>> s[0]==s[-1]
False
>>> s[-1:-4]=='tion'
False
>>> len(anachronistically)+1==len(counterintuitive)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    len(anachronistically)+1==len(counterintuitive)
NameError: name 'anachronistically' is not defined
>>> word1='anachronistically'
>>> word2='counterintuitive'
>>> len(word1)+1==len(word2)
False
>>> 'misinterpretation'<'misrepresentation'
True
>>> word3='floccinaucinihilipilification'
>>> word3[0:]=='e'
False
>>> len('counterrevolution')==sum(len('counter'),len('resolution'))
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    len('counterrevolution')==sum(len('counter'),len('resolution'))
TypeError: 'int' object is not iterable
>>> len('counterrevolution')==len('counter')+len('resolution')
True
>>> a=6
>>> b=7
>>> c=sum(a, b)/2
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    c=sum(a, b)/2
TypeError: 'int' object is not iterable
>>> c=(a+b)/2
>>> c
6.5
>>> inventory=['paper','staples','pencils']
>>> first='John'
>>> middle='Fitzgerald'
>>> last='Kennedy'
>>> fullname=first + middle + last
>>> fullname
'JohnFitzgeraldKennedy'
>>> 'JohnFitzgeraldKennedy
SyntaxError: EOL while scanning string literal
>>> first='John'
>>> middle=' Fitzgerald'
>>> last=' Kennedy'
>>> fullname=first+middle+last
>>> fullname
'John Fitzgerald Kennedy'
>>> flowers=['rose','bougainvillea','yucca','marigold','daylilly','lilly of the valley']
>>> 'potato'!=flowers
True
>>> thorny=flowers[:2]
>>> inventory
['paper', 'staples', 'pencils']
>>> thorny
['rose', 'bougainvillea']
>>> thorny=flowers[0:4]
>>> thorny
['rose', 'bougainvillea', 'yucca', 'marigold']
>>> thorny=flowers[:3]
>>> thorny
['rose', 'bougainvillea', 'yucca']
>>> poisonous=flowers[-1]
>>> poisonous
'lilly of the valley'
>>> dangerous=thorny+poisonous
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    dangerous=thorny+poisonous
TypeError: can only concatenate list (not "str") to list
>>> dangerous= thorny + poisonous
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    dangerous= thorny + poisonous
TypeError: can only concatenate list (not "str") to list
>>> dangerous=thorny[0:]+poisonous[0:]
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    dangerous=thorny[0:]+poisonous[0:]
TypeError: can only concatenate list (not "str") to list
>>> dangerous=(thorny+poisonous)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    dangerous=(thorny+poisonous)
TypeError: can only concatenate list (not "str") to list
>>> thorny
['rose', 'bougainvillea', 'yucca']
>>> poisonous
'lilly of the valley'
>>> poisonous=flowers[-1:]
>>> poisonous
['lilly of the valley']
>>> dangerous=thorny+poisonous
>>> dangerous
['rose', 'bougainvillea', 'yucca', 'lilly of the valley']
>>> answers=['Y','N','N','Y','N','Y','Y','Y','N','N','N']
>>> numYes=answers['Y']
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    numYes=answers['Y']
TypeError: list indices must be integers or slices, not str
>>> numYes='Y' in answers
>>> numYes
True
>>> numYes=sum('Y' in answers)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    numYes=sum('Y' in answers)
TypeError: 'bool' object is not iterable
>>> numYes=answers.count('Y')
>>> numYes
5
>>> numNo=answers.count('N')
>>> numNo
6
>>> numYes/answers.total
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    numYes/answers.total
AttributeError: 'list' object has no attribute 'total'
>>> numAll=answers.count('N', 'Y')
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    numAll=answers.count('N', 'Y')
TypeError: count() takes exactly one argument (2 given)
>>> numAll = numYes+numNo
>>> numAll
11
>>> percentYes=(numYes/numAll)*100
>>> percentYes
45.45454545454545
>>> answers.sort
<built-in method sort of list object at 0x0000015C47CC74C8>
>>> sort(answers)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    sort(answers)
NameError: name 'sort' is not defined
>>> answers.sort()
>>> print(answers.sort())
None
>>> answers
['N', 'N', 'N', 'N', 'N', 'N', 'Y', 'Y', 'Y', 'Y', 'Y']
>>> f=answers.index('Y')
>>> f
6
>>> s = 'cat'
>>> s2=s.reverse()
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    s2=s.reverse()
AttributeError: 'str' object has no attribute 'reverse'
>>> s='cat'
>>> s.reverse()
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    s.reverse()
AttributeError: 'str' object has no attribute 'reverse'
>>> s.reverse('cat')
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    s.reverse('cat')
AttributeError: 'str' object has no attribute 'reverse'
>>> s=['c','a','t']
>>> s
['c', 'a', 't']
>>> s.reverse()
>>> s
['t', 'a', 'c']
>>> dartboard=pi*10**2
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    dartboard=pi*10**2
NameError: name 'pi' is not defined
>>> import math
>>> pi
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    pi
NameError: name 'pi' is not defined
>>> help(math)
Help on built-in module math:

NAME
    math

DESCRIPTION
    This module is always available.  It provides access to the
    mathematical functions defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
    
    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
    
    asin(x, /)
        Return the arc sine (measured in radians) of x.
    
    asinh(x, /)
        Return the inverse hyperbolic sine of x.
    
    atan(x, /)
        Return the arc tangent (measured in radians) of x.
    
    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.
        
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(x, /)
        Return the inverse hyperbolic tangent of x.
    
    ceil(x, /)
        Return the ceiling of x as an Integral.
        
        This is the smallest integer >= x.
    
    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.
        
        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.
    
    cos(x, /)
        Return the cosine of x (measured in radians).
    
    cosh(x, /)
        Return the hyperbolic cosine of x.
    
    degrees(x, /)
        Convert angle x from radians to degrees.
    
    erf(x, /)
        Error function at x.
    
    erfc(x, /)
        Complementary error function at x.
    
    exp(x, /)
        Return e raised to the power of x.
    
    expm1(x, /)
        Return exp(x)-1.
        
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(x, /)
        Return the absolute value of the float x.
    
    factorial(x, /)
        Find x!.
        
        Raise a ValueError if x is negative or non-integral.
    
    floor(x, /)
        Return the floor of x as an Integral.
        
        This is the largest integer <= x.
    
    fmod(x, y, /)
        Return fmod(x, y), according to platform C.
        
        x % y may differ.
    
    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).
        
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.
        
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(x, /)
        Gamma function at x.
    
    gcd(x, y, /)
        greatest common divisor of x and y
    
    hypot(x, y, /)
        Return the Euclidean distance, sqrt(x*x + y*y).
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.
    
    ldexp(x, i, /)
        Return x * (2**i).
        
        This is essentially the inverse of frexp().
    
    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(x, /)
        Return the base 10 logarithm of x.
    
    log1p(x, /)
        Return the natural logarithm of 1+x (base e).
        
        The result is computed in a way which is accurate for x near zero.
    
    log2(x, /)
        Return the base 2 logarithm of x.
    
    modf(x, /)
        Return the fractional and integer parts of x.
        
        Both results carry the sign of x and are floats.
    
    pow(x, y, /)
        Return x**y (x to the power of y).
    
    radians(x, /)
        Convert angle x from degrees to radians.
    
    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.
        
        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.
    
    sin(x, /)
        Return the sine of x (measured in radians).
    
    sinh(x, /)
        Return the hyperbolic sine of x.
    
    sqrt(x, /)
        Return the square root of x.
    
    tan(x, /)
        Return the tangent of x (measured in radians).
    
    tanh(x, /)
        Return the hyperbolic tangent of x.
    
    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.
        
        Uses the __trunc__ magic method.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    (built-in)


>>> pi
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    pi
NameError: name 'pi' is not defined
>>> dartboard=3.14159*(10**2)
>>> dartboard
314.159
>>> dartboardX=0,1,2,3,4,5,6,7,8,9,10
>>> dartboardY=0,1,2,3,4,5,6,7,8,9,10
>>> 0 in dartboardX and 0 in dartboardY
True
>>> 10 in dartboardX and 10 in dartboardY
True
>>> dartboardX.append(-1,-2,-3,-4,-5,-6,-7,-8,-9,-10)
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    dartboardX.append(-1,-2,-3,-4,-5,-6,-7,-8,-9,-10)
AttributeError: 'tuple' object has no attribute 'append'
>>> dartboardX=-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10
>>> dartboardY=-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10
>>> 0 in dartboardX and 0 in dartboardY
True
>>> 10 in dartboardX and 10 in dartboardY
True
>>> 6 in dartboardX and -6 in dartboardY
True
>>> -7 in dartboardX and 8 in dartboardY
True
>>> 'e' in 'floccinaucinihilipilification'
False
>>> s='cat'
>>> s.reverse()
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    s.reverse()
AttributeError: 'str' object has no attribute 'reverse'
>>> str.reverse(s)
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    str.reverse(s)
AttributeError: type object 'str' has no attribute 'reverse'
>>> s[-1:0]
''
>>> s
'cat'
>>> s[:-1:]
'ca'
>>> s[-1:]
't'
>>> s[-1:1]
''
>>> s[-1:-3
      ]
''
>>> s[::1]
'cat'
>>> s[::-1]
'tac'
>>> 
