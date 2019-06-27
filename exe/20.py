#1
str=input("Enter string:")
n=int(input("Enter numbers of copies:"))
def copier(str,n):
    exe=""
    for i in range(n):
        exe=exe+str
    return exe
print(copier(str,n))

#2

str=input("Enter string:")
n=int(input("Enter nuber:"))
print(str*n)

