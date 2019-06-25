#1
def valuecheck1(num,list):
    return num in list

print(valuecheck1(3,[1,2,3,4,5,6]))


#2
list=[1,2,3,4,5,6]
num=10
def valuecheck2(num,list):
    return num in list
print(valuecheck2(num,list))


#3
def valuecheck3(val,list):
    for i in list:
        if val == i:
            return True
    return False

print(valuecheck3(3,[1,2,3,4,5,6,7,8]))