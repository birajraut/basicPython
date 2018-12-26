from __future__ import print_function
num=29
prime=True
for test in range(2,num):
    if(num%test==0 and num!=test):
        print(num,"equal",test,"*",num/test)
        break
        prime=False
        if prime:
            print(num,"is a prime number")
        else:
            print(num,"is not a prime number")
else:
    print(num,"is a prime number")