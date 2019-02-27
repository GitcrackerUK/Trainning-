#1
# Write a Python program to print the following string in a specific format

#Sample string:

#docstring
"""Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"""
#docstring

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
# Write a Python program to display the examination schedule.
# (extract the date from exam_st_date)

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
# Write a Python program to print the documents
# (syntax, description etc.) of Python built-in function(s).

# print(abs.__doc__)
# print(map.__doc__)

#12
# Write a Python program to print the calendar of a given month and year.

# import calendar
# month=int(input("Insert month:"))
# year=int(input("Insert year:"))
# print(calendar.month(year,month))


#13
# #Write a Python program to print the following here document.

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

# r=6
# v=4/3*pi*(r**3)
# print(v)

#16
# Write a Python program to get the difference between a given number and 17,
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
# def difference(x):
#     if x > 17 :
#         out=2*(x-17)
#     else:
#         out=17-x
#     return out
#
# print(difference(3))
# print(difference(16))
# print(difference(18))
# print(difference(25))


#17.
# Write a Python program to test whether a number is within
# 100 of 1000 or 2000.



# def within(x):
# return((abs(1000-x)<=100) or (abs(2000 - x)<=100))


# print(within(400))
# print(within(1050))
# print(within(2050))
# print(within(950))

#18.
# Write a Python program to calculate the sum of three given numbers,
# if the values are equal then return thrice of their sum.

#A)
# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# c=int(input("Enter a number:"))
# if a==b==c:
#     print((a+b+c)*3)
# else:
#     print(a+b+c)
#B)
# def sum_trice(x,y,z):
#     if x==y==z:
#         return ((x+z+y)*3)
#     else:
#         return (x+z+y)
#
#
# print(sum_trice(3,3,3))
# print(sum_trice(2,4,5))

#19.
# Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.

#A)
# string1=input("Type in text:")
# if "Is" not in string1 :
#     string2=("Is"+" "+ string1)
#     print(string2)
# else :
#     print(string1)
    
# Type in text: Is weather good today?
# Is weather good today?
#
# Type in text:weather good today?
# Is weather good today?

#B)

# def new_string(str):
#   if len(str) >= 2 and str[:2] == "Is":
#     return str
#   return "Is" + str
#
# print(new_string("Array"))
# print(new_string("Is Empty"))

#20
# Write a Python program to get a string
# which is n (non-negative integer) copies of a given string.

#A)
# u=input("Insert text:")
# y=int(input("Insert number of coppies:"))
# print((str(u)+" ")*y)

#B)
# def copies(str,n):
#     return(str*n)
#
# print(copies("text",4))

#C)
# def str_copies(str,n):
#     result=""
#     for i in range(n):
#         result=result+str
#     return result
# print(str_copies("tato lato",5))

#21
# Write a Python program to find whether a given number (accept from the user)
# is even or odd, print out an appropriate message to the user.

#A)
# z=int(input("Enter a number:"))
# if z % 2==0:
#     print(z,"is even. ")
# else:
#     print(z,"is odd!!")

#B)

# num = int(input("Enter a number: "))
# mod = num % 2
# print(mod)
# if mod > 0:
#     print(num,"is an odd number.")
# else:
#     print(num,"is an even number.")

#22
# Write a Python program to count the number 4 in a given list

#A)
# list1=[2,3,5,4,6,7,4,4,4,8]
# list2=[]
# for i in list1:
#     if i == 4:
#         list2.append(i)
# print(len(list2))

#B)
# list1=[2,3,5,4,6,7,4,4,4,8]
# def count_num_4(list1):
#     summary=[]
#     for i in list1:
#         if i == 4:
#             summary.append(i)
#     return len(summary)
#
#
# print(count_num_4(list1))

#23
# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.


def substring_copy(str, n):
    summary=[]
    if 2 >= len(str):
        summary=(str*n)
    if 2 < len(str):
        summary=(str[:2]*n)
    return summary



print(substring_copy('abcdef', 2))
print(substring_copy('p', 3));