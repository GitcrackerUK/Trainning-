1
# Write a Python program to print the following string in a specific format

#Sample string:
"""Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"""

#Output expected:
"""Twinkle, twinkle, little star,
	 How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	bHow I wonder what you are"""

# To print String in new line, need be used \n to make extra horizontal tab need be used \n\t

#print("Twinkle , twinkle, litle star,\n\t How I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

"""Twinkle, twinkle, little star,
	 How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	bHow I wonder what you are"""

2
# Write a Python program to get the Python version you are using.

# To check python version need be used sys.version command
# import sys
# print(sys.version)
#
# 3.6.7 (default, Oct 22 2018, 11:32:17)
# [GCC 8.2.0]

# 3
# Write a Python program to display the current date and time.

#To disply current date and time need be imported datetime module

# import datetime
# x = (datetime.datetime.now())
# print("Current date and time: ")
# print(x.strftime("%Y-%m-%d\n%H:%M:%S"))

#4
#Write a Python program which accepts
# the radius of a circle from the user and compute the area.

# from math import pi
# x=float(input("Enter radius"))
# y=pi*(x**2)
# print("Area of the circle with radius", x ,"is:",y)

#5
# Write a Python program which accepts the user's first and last name
# and print them in reverse order with a space between them.

# fname=input("Enter your first name, please:")
# lname=input("Enter your last  name, please:")
# print("Hello",lname,fname)

#6
# Write a Python program which accepts a sequence of comma-separated
# numbers from user and generate a list and a tuple with those numbers.

# base=input("Enter list of numbers separated by commas:")
# list=base.split(",")
# tuple=tuple(list)
# print("List:",list)
# print("Tuple:",tuple)

#7
# Write a Python program to accept
# a filename from the user and print the extension of that.

# filename = input("Enter file name with extension:")
# f=filename.split(".")
#
# print("Output:" + f[1])


#pon25.02

#8
# Write a Python program to display the first and last colors
# from the following list.

# color_list = ["Red","Green","White" ,"Black"]
#
# print(color_list[0])
# print(color_list[3])
#
# print((color_list[0]),(color_list[3]))

#9

# exam_st_date = (11, 12, 2014)
# print("The examination will start from: %i/%i/%i" %exam_st_date)

#10
# Write a Python program that accepts
# an integer (n) and computes the value of n+nn+nnn.

# n=5
# n2=str(n,n)
# n3=str(n,n,n)
# print((n)+(n2)+(n3))

#11

# print(abs.__doc__)
# print(map.__doc__)

#12

# import calendar
# month=int(input("Insert month:"))
# year=int(input("Insert year:"))
# print(calendar.month(year,month))


#13

# #Write a Python program to print the following here document.
#
# print("""a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example""")

#14

# Write a Python program to calculate number of days between two dates
#A)
# from datetime import date
# fd=int(input("insert day:"))
# fm=int(input("insert month:"))
# fy=int(input("insert year:"))
# ld=int(input("insert day:"))
# lm=int(input("insert month:"))
# ly=int(input("insert year:"))
# date1=date(fy,fm,fd)
# date2=date(ly,lm,ld)
# wynik=date2-date1
# print(wynik.days)

#B)
#from datetime import date
#f_date = date(2014, 7, 2)
#l_date = date(2014, 7, 11)
#delta = l_date - f_date
#print(delta.days)

#15
# Write a Python program to get the volume of a sphere with radius 6.

# from math import pi
#
# r=6
# v=4/3*pi*(r**3)
# print(v)

#16

#Write a Python program to get the difference between a given number and 17,
# if the number is greater than 17 return double the absolute difference.

#A)
# a=int(input("Type number:"))
# b=17
# if a > b:
#     output=2*(a-b)
# else:
#     output=b-a
#
# print(output)

#B)
# def difrence(x):
#     if x > 17 :
#         out=2*(x-17)
#     else:
#         out=17-x
#     return out
#
# print(difrence(3))
# print(difrence(16))
# print(difrence(18))
# print(difrence(25))
#
#C)


#17. Write a Python program to test whether a number is within
# 100 of 1000 or 2000.



def within(x):
    if x <= 100:
        print(x,"is within 100")
    if x < 1000:
        print(x,"is within 1000")
    if x <2000:
        print(x,"is within 2000")
    return



print(within(400))






