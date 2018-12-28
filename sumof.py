x = [1,2,3,4,5,6,7,8,9]
sumeven=0
sumodd=0
for n in x:
 if(n%2!=0):
     sumeven = sumeven + n
 elif(n%2==0):
     sumodd = sumodd + n

print("sum of even =",sumeven)
print("sum of odd =",sumodd)
