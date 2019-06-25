

#1

def copier(str,n):
    if 1 == len(str):
        return (str*n)
    else :
        return (n*str[:2])
print(copier("saba",3))
print(copier("s",3))

#2

def substring_copy(str, n):
    flen = 2
    if flen > len(str):
        flen = len(str)
    substr = str[:flen]

    result = ""
    for i in range(n):
        result = result + substr
    return result
print(substring_copy('abcdef', 2))
print(substring_copy('p', 3));