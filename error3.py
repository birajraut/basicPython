from __future__ import print_function
while True:
    try:
        print('let us solve the equn (x/2)/(x-y)')
        x=float(input('please enter a value for x='))
        y=float(input('please enter a value for y='))
        if x==0 or y==0:
            break
        z=(x/2)/(x-y)
        print('Solving (x/2)/(x-y) for value x=',x,'and y',y,'we get the result=',z)
    except ZeroDivisionError as e:
        print('there was an unknown error with the code')
        print('you keyed in a value that caused',' division by zero')