#for loop

x=[]
for i in range(1500,2701): # creation of loop in range between 1500 and 2701
    if (i % 7==0) and (i % 5 ==0): #condition that if number in range from above meet cryteria (is divisiable by 7 and 5) value should be passed further down.
        x.append(str(i))  #value filtered by condition above is stored in varible x  as a string.
print(','.join(x))  #values from varible x is separeted by comma and printed
print(len(x))      #this method is printing quantity of vules in variable