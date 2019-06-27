def stringls(str):
    if len(str) >= 2 and str[:2]=="Is":
        return str
    return "Is" + str

print(stringls("Array"))
print(stringls("Tasmania"))
print(stringls("IsEmpty"))
