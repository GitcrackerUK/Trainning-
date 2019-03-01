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

# Type in text:weather good today?
# Is weather good today?

#B)

# def new_string(str):
#   if len(str) >= 2 and str[:2] == "Is":
#     return str
#   return "Is" + str

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


# print(count_num_4(list1))

#23
# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.


# def substring_copy(str, n):
#     summary=[]
#     if 2 >= len(str):
#         summary=(str*n)
#     if 2 < len(str):
#         summary=(str[:2]*n)
#     return summary

#print(substring_copy('abcdef', 2))
# print(substring_copy('p', 3));


#24
# Write a Python program to test whether a passed letter is a vowel or not.

# letter=input("Enter one letter:")
# if letter == "A" or letter=="E" or letter == "I" or letter == "O" or letter == "U" or letter == "a" or letter == "e" or letter == "i" or letter=="o":
#     print("Letter",letter,"is a vowel." )
# else:
#     print("Letter",letter,"is constant.")

#25
# Write a Python program to check whether a specified value is contained in a group of values.

# list=[2,3,4,5,6,7,8,9]
# def value_con(list,x):
#     if x in list:
#         return True
#     else:
#         return False
#
#
# print(value_con(list,5))
# print(value_con(list,1))
# print(value_con([12,3,4,6,8],5))

#26
# Write a Python program to create a histogram from a given list of integers.

# def histogram(item) :
#     for i in item:
#         output =''
#         while( i > 0):     #creating loop which will run until specified numper will be reduced to 0
#             output += "*"  #adding * every loop
#             i = i - 1      #reducing number i by 1
#             #print(output) # placing print inside while loop resulting printing of all numbers up to specified
#         print(output)      #placing print at the end of while loop resulting in histogram just of numbers specified
#     #print(output)         #moving print under for loop result printing out just histogram of last number
#
# histogram([5,1,2,1,6,7,8,9])



# list=[1,2,3,4,5,6,7,8,3,4,5]
# def histo(x):
#     for i in x:
#         out=''
#         while i > 0:
#             out += '@'
#             i = i - 1
#         print(out)
# histo(list)


#27
#  Write a Python program to concatenate all elements in a list into a string and return it.

#list1=[1,2,3,4,5,6,7]
# def concat(list1):
#     result=''
#     for i in list1:
#         result += str(i) #This line is adding i(item) one by one to varible "result".
#     return result
# print(concat(list1))
#
# #int is not iterable!!!


#28

# Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing
# if any numbers that come after 237 in the sequence.


# numbers = [
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
#     958,743, 527
#     ]

# A)
#  def even(numbers):
#      evenlist=[]
#      for i in numbers: #creating loop to iterate over list "numbers"
#          if i == 237: #checking if i is int 237
#              break    # breaking a loop if i is int 237
#          if i % 2== 0 :
#              evenlist.append(i)
#      return evenlist
#  print(even(numbers))


# B)
#  for x in numbers:
#      if x == 237:
#          print(x)
#          break;
#      elif x % 2 == 0:
#          print(x)

#29

# color_list_1 = (["White", "Black", "Red"])
# color_list_2 = (["Red", "Green"])
#
# """print(set(color_list_1).intersection(set(color_list_2)))""" # this is way to extract same items from lists.
#
# #print(set(color_list_1)-(set(color_list_2))) #To extract only unic item without duplcates in a list need be used set
#
#
# x=[2,3,4,4,4,4,43,2,34,4,5,7,5444,5,4,3,3,222,3,5444]
# y=[3,4,3,2,3,4,5,6,7,7,6,5,4,34,7]
# print(set(x))
#
# # x=("w","w","e","e","w","w","e","w","w",)
# # print(x)
#
# print((set(x))-(set(y)))

#30

# def triangle_area(base,height):
#     area=base*height/2
#     return area
#
# print(triangle_area(5,10))

#31 !!!


# def gcd(a,b):
#     c = 1
#     a,b = max(a,b),min(a,b)
#     while c != 0:
#         c = a%b
#         a,b = b,c
#     return a
# print(gcd(270,300))

#32 !!!

# Write a Python program to get the least common multiple (LCM) of two positive integers

# def lcm(x, y):
#    if x > y:
#        z = x
#    else:
#        z = y
#
#    while(True):
#        if((z % x == 0) and (z % y == 0)):
#            lcm = z
#            break
#        z += 1
#
#    return lcm
# print(lcm(4, 6))
# print(lcm(15, 17))


# def lcm(a):
#     if a % 2== 0:
#         a=a/2
#         if a % 2==0:
#             a=a/2
#     if a % 3==0:
#         a=a/3
#     if a % 4==0:
#         a=a/4
#     if a % 5==0:
#         a=a/5
#     if a % 6==0:
#         a=a/6
#     if a % 7==0:
#         a=a/7
#     if a % 8==0:
#         a=a/8
#     if a % 9==0:
#         a=a/9
#     if a % 10==0:
#         a=a/10
#     return int(a)

# 33.
#  Write a Python program to sum of three given integers. However, if
#     two values are equal sum will be zero.

# def summary(x,z,y):
#     if x==z or z==y:
#         return 0
#     else:
#         return x+z+y
#
# print(summary(3,4,5))
# print(summary(2,2,3))
# print(summary(2,3,3))

# 34
# Write a Python program to sum of two given integers.
# However, if the sum is between 15 to 20 it will return 20.

# def sum_two_except_bt_15_20(z,x):
#     y=z+x
#     if y >= 15 and y <= 20:
#         return 20
#     else:
#         return y
#
# print(sum_two_except_bt_15_20(7,7))
# print(sum_two_except_bt_15_20(7,8))
# print(sum_two_except_bt_15_20(9,7))
# print(sum_two_except_bt_15_20(13,9))

# 35
# Write a Python program that will return true
# if the two given integer values are equal or their sum or difference is

# def equal(a,z):
#     if a == z or a+z==5 or a-z==5:
#         return True
#     else:
#         return False
#
# print(equal(2,5))
# print(equal(2,3))
# print(equal(10,5))
# print(equal(9,5))

#36
#Write a Python program to add two objects if both objects are an integer type.

#A)
# def add_int(a,b):
#     if a is int(a) and b is int(b):
#         return a + b
#     else:
#         return "One or both of inputs are not integers!!"
#
# print(add_int(3,5))
# print(add_int(13,5))
# print(add_int(3.0,5.0))
# print(add_int(3.,5.0))
# print(add_int(3.,55))

#B)
# def sum_variable(a,b):
#     if not (isinstance(a,int)and isinstance(b,int)):
#         return "Input it's not a variable!!"
#     return a + b
#
# print(sum_variable(4,4))
# print(sum_variable(4,4.0))

#37
# Write a Python program to display your details like
# name, age, address in three different lines.



# def personal_info():
#     name, age="Pawel",33
#     adress="4 Bounty Nash Court, Coronation Square"
#     return("name:{}\nage:{}\nadress:{}".format(name,age,adress)) # Calling dictionary by name and in specific format
#
# print(personal_info())


# #del dict['Name']  remove entry with key 'Name'
# dict.clear()       remove all entries in dict
# del dict           delete entire dictionary

#38
#Write a Python program to solve (x + y) * (x + y).

# def solve(x,y):
#     result = (x+y)*(x+y)
#     return ("({}+{})^2)={}".format(x,y,result)) # Calling result in specific format.
#
# def solve2(x,y):
#     return(x+y)**2
#
# print(solve(3,7))
# print(solve2(4,3))
# print(solve2(12,4))

#39  !!!!!!!!!!!!!!!!!!!
# Write a Python program to compute the future value
# of a specified principal amount, rate of interest, and a number of years.
# amt=10000
# int=3.5
# y=7
# def apr_calc(amt,int,y):
#     intr=((1+(0.01*int)) ** y)
#     return round(amt*intr)
#
# print(apr_calc(amt,int,y))
#
#
# def calc(amt,int,y):
#     for i in range(y):
#         amt += amt*0.035
#     return(amt)
# print(calc(amt,int,y))

#40
#Write a Python program to compute the distance
# between the points (x1, y1) and (x2, y2)




#41
#Write a Python program to check whether a file exists.

import os

# print(os.path.isfile('./Exercises , Basic Part 1.py'))  # True
# print(os.path.isfile('file.txt'))    # False
# print(os.path.isfile('./link.txt'))  # False
# print(os.path.isfile('./fake.txt'))  # False
# print(os.path.isfile('./dir')    )   # False
# print(os.path.isfile('./sym')    )   # False

#42
#Write a Python program to determine if a Python
# shell is executing in 32bit or 64bit mode on OS.

# import struct
# print(struct.calcsize("P")*8)
#
# import platform
# print(platform.architecture()[0])
#
# import sys
# print(sys.maxsize > 2**32)  # it should display True in case of 64bit and False in case of 32bit

#43
#