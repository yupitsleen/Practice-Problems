""" 
Fizz Buzz - Write a program that prints the numbers from 1 to 100. 
But for multiples of three print “Fizz” instead of the number and 
for the multiples of five print “Buzz”. For numbers which are 
multiples of both three and five print “FizzBuzz”. 
1.print nums 1 to 100
2.print multiples of 3
3.print multiples of 5
4. print multiples of 3 and 5
5. replace with fizz, buzz, and fizzbuzz
6.refactor
"""

def fizzbuzz():
    
    for num in range(1,101):
        #4
        if num%5==0 and num%3==0:
            print('fizzbuzz')
        #2
        elif num%3==0:
            print('fizz')
        #3
        elif num%5==0:
            print('buzz')
        
        #1
        else:
            print (num)
    
    

def fizzbuzz_recursive(num):

    if num == 100:
        print (num)
        return
    #4
    if num%5==0 and num%3==0:
        print('fizzbuzz')
    #2
    elif num%3==0:
        print('fizz')
    #3
    elif num%5==0:
        print('buzz')
    #1
    else:
        print (num)

    fizzbuzz_recursive(num+1)




fizzbuzz()
fizzbuzz_recursive(1)
