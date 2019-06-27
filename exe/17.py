n=int(input("Enter number:"))
def near(n):
    return (abs(n-1000)<=100) or (abs(n-2000)<=100)

print(near(n))


print(near(1000))
print(near(900))
print(near(800))
print(near(2200))