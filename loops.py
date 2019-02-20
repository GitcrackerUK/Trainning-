#for loop
from typing import List

x: List[str]=[]
for i in range(1500,2701): # creation of loop in range between 1500 and 2701
    if (i % 7==0) and (i % 5 ==0): #condition that if number in range from above meet cryteria (is divisiable by 7 and 5) value should be passed further down.
        x.append(str(i))  #value filtered by condition above is stored in varible x  as a string.
print(','.join(x))  #values from varible x is separeted by comma and printed
print(len(x))      #this method is printing quantity of vules in variable x


test=[]
for i in range(0,150):
    if i % 6 == 0:
        test.append(str(i))
print(test)
print(','.join(test))



three=[]
for i in range(200,240):
    if i % 3 ==0:
        three.append(str(i))
print('.'.join(three))




session=[]
for i in range (10,100):
    if (i % 7 ==0) and (i % 9 == 0):
        session.append(str(i))
print(session)


totu=[]
tot=[]
for i in range (0,100):
    if (i % 3 ==0) and ( i % 5 == 0):
        tot.append(str(i))
totu=(','.join(tot))
print(totu)













x=[]
for i in range(1500,2701):
    if (i % 7 == 0) and (i % 5 == 0):
        x.append(str(i))

print('\n'.join(x))
print(len(x))









































