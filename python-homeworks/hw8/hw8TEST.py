M
mushroom
onion
garlic

L
calamari
garlic

S


# hw8TEST.py

above lines are user inputs to be used for code
that requires user input


>>> from hw8 import *

##### Pizza #####


>>> pie = Pizza()
>>> pie
Pizza('M',set())
>>> pie.setSize('L')
>>> pie.getSize()
'L'
>>> pie.addTopping('pepperoni')
>>> pie
Pizza('L',{'pepperoni'})
>>> pie.addTopping('anchovies')
>>> pie.addTopping('mushrooms')
>>> pie==Pizza('L',{'anchovies', 'mushrooms', 'pepperoni'})
True
>>> pie.addTopping('pepperoni')
>>> pie==Pizza('L',{'anchovies', 'mushrooms', 'pepperoni'})
True
>>> pie.removeTopping('anchovies')
>>> pie==Pizza('L',{'mushrooms', 'pepperoni'})
True
>>> pie.price()
16.65

Note: In the following code,
p==p2 shoudl be False.   If True
than they are sharing the same set (or list) of toppings

You need to make sure that the set() constructor is
called in all cases in the body of the Pizza
constructor.   See course notes for the Queue class.

>>> p = Pizza()
>>> p2 = Pizza()
>>> p.addTopping('mushroom')
>>> p2.addTopping('onion')
>>> p.addTopping('mushroom')
>>> p
Pizza('M',{'mushroom'})
>>> p2
Pizza('M',{'onion'})
>>> p==p2   # see note in TEST file
False
>>> 
# reroute stdin #

code below directs input to be received from above
should not cause an error

>>> import sys
>>> si = sys.stdin
>>> sys.stdin = open('hw8TEST.py')


##### orderPizza #####
>>> orderPizza()==Pizza('M',{'garlic', 'onion', 'mushroom'})
Welcome to Python Pizza!
What size pizza would you like (S,M,L): Type topping to add (or Enter to quit): Type topping to add (or Enter to quit): Type topping to add (or Enter to quit): Type topping to add (or Enter to quit): Thanks for ordering!
Your pizza costs $14.299999999999999
True
>>> orderPizza()==Pizza('L',{'calamari', 'garlic'})
Welcome to Python Pizza!
What size pizza would you like (S,M,L): Type topping to add (or Enter to quit): Type topping to add (or Enter to quit): Type topping to add (or Enter to quit): Thanks for ordering!
Your pizza costs $16.65
True
>>> orderPizza()==Pizza('S',set())
Welcome to Python Pizza!
What size pizza would you like (S,M,L): Type topping to add (or Enter to quit): Thanks for ordering!
Your pizza costs $6.25
True

#stdin back #

put stdin back to original, again, shouldnt cause error
>>> sys.stdin = si  # return stdin


##### Stack #####            

>>> s = Stack()
>>> s.push('apple')
>>> s
Stack(['apple'])
>>> s.push('pear')
>>> s.push('kiwi')
>>> s
Stack(['apple', 'pear', 'kiwi'])
>>> top = s.pop()
>>> top
'kiwi'
>>> s
Stack(['apple', 'pear'])
>>> len(s)
2
>>> s.isEmpty()
False
>>> s.pop()
'pear'
>>> s.pop()
'apple'
>>> s.isEmpty()
True
>>> s = Stack(['apple', 'pear', 'kiwi'])
>>> s = Stack(['apple', 'pear', 'kiwi'])
>>> s[0]
'apple'
>>> 

check that Stacks constructed without a list remain distinct
if you receive an error on s2 then you probably need to use a
default argument of None in __init__
(see the Queue class developed in class for an example)

>>> s = Stack()
>>> s.push('apple')
>>> s
Stack(['apple'])
>>> s2 = Stack()
>>> s2.push('pear')
>>> s2  # if this fails - see the TEST file for explanation
Stack(['pear'])


##### parenthesesMatch #####


>>> parenthesesMatch('(){}[]')
True
>>> parenthesesMatch('{[()]}')
True
>>> parenthesesMatch('((())){[()]}')
True
>>> parenthesesMatch('(}')
False
>>> parenthesesMatch(')(][') # right number, but out of order
False
>>> parenthesesMatch('([)]') # right number, but out of order
False
>>> parenthesesMatch('({])')
False
>>> parenthesesMatch('((())')
False
>>> parenthesesMatch('(()))')
False
