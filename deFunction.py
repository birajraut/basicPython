import math
# def exp(x,y):
#     z = x**y
#     print(z)
#
# def add(a, b):
#     s = a + b
#     print(s)
#
# def fib(n):
#     a,b =0,1
#     while b<n:
#         print(b)
#         a,b=b,a+b
#
# def calfib(n):
#     result=[]
#     a,b=0,1
#     while b<n:
#         result.append(b)
#         a,b=b,a+b
#     return result

# def multitable(x,y):
#     for line in range(1,y+1):
#         for table in range(1,x+1):
#             print (line * table,'\t',end="")
#         print("\n")
#  for line in range(1,6):
#      for table in range(1,6):
#          print (line * table,'\t')
#     print
# a=int(input('Enter the 1st number='))
# b=int(input('Enter the 2nd number='))
# multitable(a,b)

def calcircumference(r):
    a=2*math.pi*r
    return a
