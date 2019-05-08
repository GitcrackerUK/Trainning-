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
# if the two given integer values are equal or their sum or difference is 5

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

#import os

# print(os.path.isfile('./Exercises , Basic Part 1.py'))  # True
# print(os.path.isfile('file.txt'))    # False
# print(os.path.isfile('./link.txt'))  # False
# print(os.path.isfile('./fake.txt'))  # False
# print(os.path.isfile('./dir')    )   # False
#print(os.path.isfile('./pam_environment')    )   # False

#42
# Write a Python program to determine if a Python
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
# Write a Python program to get OS name, platform and release information.

# import os,platform
#
#
# print(os.name)
# print(platform.system())
# print(platform.release())

#44
# Write a Python program to locate Python site-packages.

# import site
# print(site.getsitepackages())

#45 !!!!!

# Write a python program to call an external command in Python.

# from subprocess import call
#
# call(["ls", "-l"])

#46

# Write a python program to get the path and name of the file that is currently executing.
# import os
# print(os.path.abspath(__file__))

#47

# Write a Python program to find out the number of CPUs using

# import multiprocessing
# print(multiprocessing.cpu_count())

#48

# Write a Python program to parse a string to Float or Integer.

# a=123
# a=float(a)
# print(a)
# a=int(a)
# print(a)

#49

#Write a Python program to list all files in a directory in Python

# from os import listdir
# from os.path import isfile, join
# import os
# print(os.path.abspath(__file__))
# fl=[f for f in listdir("/home/gitcracker") if isfile(join("/home/gitcracker", f))]
# print(fl)

#50 Write a Python program to print without newline or space

# for i in range(0,10):
#     print("*",end="")
# print("\n")

#51 Write a Python program to determine profiling of Python programs.

# import cProfile
#
# def sum():
#     a="abcdde"
#     b="absdss"
#     print(  a,"\n",b)
# cProfile.run("sum()")

#52 Write a Python program to print to stderr !!!


#53 Write a python program to access environment variables !!!

# import os
# print(os.environ)

#54 Write a Python program to get the current username

# import getpass
# print(getpass.getuser())

#55 Write a Python to find local IP addresses using Python's stdlib

#1
# import socket
# print(socket.gethostbyname(socket.gethostname()))

#2
# print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
# if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)),
# s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
# socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

#56 Write a Python program to get height and the width of console window.

# #!/usr/bin/env python
# import os
# import shlex
# import struct
# import platform
# import subprocess
#
#
# def get_terminal_size():
#     """ getTerminalSize()
#      - get width and height of console
#      - works on linux,os x,windows,cygwin(windows)
#      originally retrieved from:
#      http://stackoverflow.com/questions/566746/how-to-get-console-window-width-in-python
#     """
#     current_os = platform.system()
#     tuple_xy = None
#     if current_os == 'Windows':
#         tuple_xy = _get_terminal_size_windows()
#         if tuple_xy is None:
#             tuple_xy = _get_terminal_size_tput()
#             # needed for window's python in cygwin's xterm!
#     if current_os in ['Linux', 'Darwin'] or current_os.startswith('CYGWIN'):
#         tuple_xy = _get_terminal_size_linux()
#     if tuple_xy is None:
#         print
#         "default"
#         tuple_xy = (80, 25)  # default value
#     return tuple_xy
#
#
#
#
#
# def _get_terminal_size_tput():
#     # get terminal width
#     # src: http://stackoverflow.com/questions/263890/how-do-i-find-the-width-height-of-a-terminal-window
#     try:
#         cols = int(subprocess.check_call(shlex.split('tput cols')))
#         rows = int(subprocess.check_call(shlex.split('tput lines')))
#         return (cols, rows)
#     except:
#         pass
#
#
# def _get_terminal_size_linux():
#     def ioctl_GWINSZ(fd):
#         try:
#             import fcntl
#             import termios
#             cr = struct.unpack('hh',
#                                fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
#             return cr
#         except:
#             pass
#
#     cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
#     if not cr:
#         try:
#             fd = os.open(os.ctermid(), os.O_RDONLY)
#             cr = ioctl_GWINSZ(fd)
#             os.close(fd)
#         except:
#             pass
#     if not cr:
#         try:
#             cr = (os.environ['LINES'], os.environ['COLUMNS'])
#         except:
#             return None
#     return int(cr[1]), int(cr[0])
#
#
# if __name__ == "__main__":
#     sizex, sizey = get_terminal_size()
#     print('width =', sizex, 'height =', sizey)

#57 Write a Python program to get execution time for a Python method

# import time
# start_time = time.time()
# get_terminal_size()
# print("--- %s seconds ---" % (time.time() - start_time))
# print(time.clock() - start_time, "seconds")


# def sum_of_n_numbers(n):
#     start_time = time.time()
#     s = 0
#     for i in range(1,n+1):
#         s = s + i
#     end_time = time.time()
#     return s,end_time-start_time

# n = 5
# print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))

#58 Write a python program to sum of the first n positive integers.

# n=input("enter a number:")
# def sum_num(n):
#     n=int(n)
#     res=(n*(n+1)/2)
#     return res
#
# print(sum_num(n))

#59 Write a Python program to convert height (in feet and inches) to centimeters.

# #1
# def converter(feet,inch):
#     hcm=(feet*30.48)+(inch*2.54)
#     print("Your hight is: %d cm" %round(hcm))
# converter(10,10)
#
# #2
# h_inch=int(input("Feet:"))
# h_ft=int(input("Inches:"))
# h_inch += h_ft * 12
#
# h_cm = h_inch * 2.54
# print("Your hight is: %d cm" %h_cm)

#60. Write a Python program to calculate the hypotenuse of a right angled triangle.

# from math import sqrt
# a=3
# b=4
# def calculate_hypo(a,b):
#     c=int(sqrt(a**2+b**2))
#     print(c)
# calculate_hypo(a,b)

#61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.

# def converter(feet):
#     inch=feet*12
#     yards=feet/3
#     miles=feet/5280.0
#     kilo=miles*1.609344
#     print(feet,"feet is:",inch,"inches")
#     print(feet,"feet is:%.2fkm"%kilo)
#     print(feet,"feet is: %.2f" %yards,"yards")
#     print(feet,"feet is: %.2f" %miles,"miles")
# converter(19341)
# kilimanjaro 19341feet


#62. Write a Python program to convert all units of time into seconds

#1

# def time_converter():
#     second=1
#     minutes=second*60
#     hour=minutes*60
#     day=hour*24
#     week=day*7
#     month=week*4
#     year=month*12
#     decade=year*10
#     century=decade*10
#     print("One minute  is:",minutes,"seconds")
#     print("One hour    is:",hour,"seconds")
#     print("One day     is:",day,"seconds")
#     print("One week    is:",week,"seconds")
#     print("One month   is:",month,"seconds")
#     print("One year    is:",year,"seconds")
#     print("One decade  is:",decade,"seconds")
#     print("One century is:" ,century,"seconds")
# time_converter()

#2

# days = int(input("Enter days:"))*3600*24
# hours = int(input("Enter hours:"))*3600
# minutes = int(input("Enter minutes:"))*60
# seconds = int(input("Enter seconds:"))

# result = days + hours + minutes + seconds
# print("Result of input is:",result,"seconds")

#63. Write a Python program to get an absolute file path.

# import os
# print(os.path.abspath("This project"))

# 64. Write a Python program to get file creation and modification date/times.

# import os
# from _datetime import datetime
# timestampm = os.path.getmtime("loops.py")
# timestampc = os.stat("loops.py").st_ctime
# #print(os.path.abspath("loops.py"))
#
# print(timestampm)
# timem=datetime.fromtimestamp(timestampm).strftime("%Y-%m-%d %H:%M:%S")
#
# print(timem)
#

# import os.path,time
# from datetime import datetime
#
# modtime= time.ctime(os.path.getmtime("Exercises , Basic Part 1.py"))
# creatimestamp= os.path.getctime("Exercises , Basic Part 1.py")
# creatime=datetime.fromtimestamp(creatimestamp).strftime("%Y-%m-%d %H:%M:%S")
# print("Modified on:",modtime)
# print("Created  on:",creatime)

#65. Write a Python program to convert seconds to
#    day, hour, minutes and seconds.

#1 from timestamp
# from _datetime import datetime
#
# def converter(seconds):
#        result=datetime.fromtimestamp(seconds).strftime("%d:%H:%M:%S")
#        print(result)
#
# converter(1554110572.9297512)
#
#2 from input

# time=int(input("Enter seconds:"))
# def converter(time):
#     day=time//(24*3600)
#     time=time%(24*3600)
#     hour=time//3600
#     time%=3600
#     minute=time//60
#     time%=60
#     seconds=time
#
#     print(time,"seconds it's:",day,"days",hour,"hours",minute,"minutes")
#     print(time,"seconds it's:",round(day),"days",round(hour),"hours",round(minute),"minutes")
#     print("d:h:m:s-> %d:%d:%d:%d" % (day,hour,minute,seconds))
# converter(time)


# #66. Write a Python program to calculate body mass index
#
# def body_mas_index(hight,weight):
#     BMI=weight/(hight*hight)
#     print(round(BMI))
# body_mas_index(1.68,63)
    
#67. Write a Python program to convert pressure in kilopascals to
#    pounds per square inch,
#    a millimeter of mercury (mmHg) and atmosphere pressure.

#1
# def pressure(kilopascal):
#
#     psi=kilopascal*0.1450377377
#     mmHg=kilopascal*7.50062
#     Atm=kilopascal*0.0098692329
#     print(kilopascal,"kilopascals converted:")
#     print("is:%.2f psi"%psi)
#     print("is:%.2f mmHg"%mmHg)
#     print("is:%.2f Atm" %Atm)
#
# pressure(2)

#2
# kpa = float(2)
# psi = kpa / 6.89475729
# mmhg = kpa * 760 / 101.325
# atm = kpa / 101.325
# print("The pressure in pounds per square inch: %.2f psi"  % (psi))
# print("The pressure in millimeter of mercury: %.2f mmHg" % (mmhg))
#print("Atmosphere pressure: %.2f atm." % (atm))

#68. Write a Python program to calculate the sum of the digits in an integer.

# 1
# x=123456
# def counter(x):
#     print(len(str(x)))
# counter(x)

# 2
# x=123456
# import math
# def counter(x):
#     count=int(math.log10(x))+1
#     print(count)

# counter(x)

#69. Write a Python program to sort
#   three integers without using conditional statements and loops.

#1

# a=2
# b=1
# c=7
# #
# def sorter(a,b,c):
#      h=max(a, max(b,c))
#      l=-max(-a,max(-b,-c))
#      m=(a+b+c) - (h+l)
#      print (l,m,h)
# sorter(a,b,c)

#2
# a=int(input("Enter first  random number:"))
# b=int(input("Enter second random number:"))
# c=int(input("Enter third random number:"))
# def sorter2(a,b,c):
#     high=max(a,max(b,c))
#     low=min(a,min(b,c))
#     mid = (a + b + c) - (high + low)
#     print("blaaaaa")
#     print("Lowest  number in a list is:%d"%low)
#     print("Middle  number in a list is:%d"%mid)
#     print("Highest number in a list is:%d"%high)
#
# sorter2(a,b,c)

#3

# a=int(input("Enter first  random number:"))
# b=int(input("Enter second random number:"))
# c=int(input("Enter third random number:"))
#
# def sorter3(a,b,c):
#     zulu=[]
#     zulu.append(a)
#     zulu.append(b)
#     zulu.append(c)
#
#     print(sorted(zulu))
#
# sorter3(a,b,c)

#70. Write a Python program to sort files by date.

# import glob
# import os
#
#
# files=glob.glob("*.txt")
# files.sort(key=os.path.getmtime)
# print("\n".join(files))


#71. Write a Python program to get a directory listing, sorted by creation date.!!!!!!


# from stat import S_ISREG, ST_CTIME, ST_MODE
# import os, sys, time
#
# #Relative or absolute path to the directory
# dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'
#
# #all entries in the directory w/ stats
# data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
# data = ((os.stat(path), path) for path in data)
#
# # regular files, insert creation date
# data = ((stat[ST_CTIME], path)
#            for stat, path in data if S_ISREG(stat[ST_MODE]))
#
# for cdate, path in sorted(data):
#     print(time.ctime(cdate), os.path.basename(path))


#72. Write a Python program to get the details of math module.

# import math
# print("\n".join(dir(math)))

#73. Write a Python program to calculate midpoints of a line.


# def mid_point(xa,xb,ya,yb):
#
#     M=(xa+xb)/2,(ya+yb)/2
#     print (M)
#
# mid_point(-3,8,5,-1)


#74 Write a Python program to hash a word.
# import base64
#
#
# base64.encodestring('peterbengtsson')

# 75. Write a Python program to get the copyright information.
# import sys
# print("\nPython Copyright Information")
# print(sys.copyright)
# print()

# 76. Write a Python program to get the command-line arguments
# (name of the script, the number of arguments, arguments) passed to a script

# import sys
#
# print("This is name of the script",sys.argv[0])
# print("This is number of arguments",len(sys.argv))
# print("The arguments are: " , str(sys.argv))



# 77. Write a Python program to test whether the system is a big-endian platform or little-endian platform.


# import sys
# print(sys.byteorder)

# 78 Write a Python program to find the available built-in modules.

# print("\n".join(dir(__builtins__)))

#79. Write a Python program to get the size of an object in bytes

#
# tb=int(input("Enter TB:"))
# gb=int(input("Enter GB:"))
# mb=int(input("Enter MB:"))
# b=int(input("Enter B:"))
#
# def object_byter(tb,gb,mb,b):
#     tb=tb*1099511627776
#     gb=(gb*1073741824)+tb
#     mb=(mb*1024)+gb
#     b=b+mb
#     print("Input converted:%d"%b)
# object_byter(tb,gb,mb,b)
#

# byte=1
# kilobyte=byte*1024
# megabyte=kilobyte*1024
# gigabyte=megabyte*1024
# terabyte=gigabyte*1024
#
# print(terabyte)


#79

# import sys
# x="pavulon"
# print(sys.getsizeof(x))
#
#
# fiirst="first"
# second="second"
# third="third"
#
# print("The size of '"+fiirst+"'= "+str(sys.getsizeof(fiirst))+"bytes")
# print("The size of '"+second+"'="+str(sys.getsizeof(second))+"bytes")
# print("The size of '"+third+ "'= "+str(sys.getsizeof(third))+ "bytes")

#80. Write a Python program to get the current value of the recursion limit.
# import sys
# print(sys.getrecursionlimit())
#
# sys.setrecursionlimit(1500) #changing recuretion limit
# print(sys.getrecursionlimit())

#81. Write a Python program to concatenate N strings.

# z="aaaaaaa"
# x="bbbbbbb"
# y=["aaaa","wwwww","QQQQQQ"]
#
# print(z+x)
# print("".join(y))
#
# y=("".join(y))
# print("all letters are:"+y)

# def concatenate(x):
    #print("".join(x))

# concatenate(y)

#82. Write a Python program to calculate the sum over a container.


# q=([10,20,30])
#
# def sum_container(x):
#     print(sum(x))
#
# sum_container(q)

#83. Write a Python program to test whether all numbers of a list is greater than a certain number.
#
# list=[1,2,3,4,5,6,7,8,99,0,]
# list1=[6,7,8,99,]
# num=5

# for i in list:
#     if num < i:
#         print("%d is smaller than list" %num)
#     else:
#         print("%d is bigger than some numbers in the list" %num)
#

# print(all(x >num for x in list1))


# print(all(x <num for x in list))

#84. Write a Python program to count the number occurrence of a specific character in a string.

# st="acnjscnsnowmowmmcpdcd"
# x="n"
# print(st.count(x))
# print(st.count("n"))

#85. Write a Python program to check if a file path is a file or a directory.
# import os
# if os.path.isfile('/usr/bin'):
#     print("It's file ")
# else:
#     print("It's directory")
#
#
#
#
# print(os.path.isfile("profileimage.jpeg"))
# print(os.path.isdir("/usr/bin"))
# print(os.path.isdir("Documents"))
#
# import os
# path="abc.txt"
# if os.path.isdir('/usr/bin'):
#     print("\nIt is a directory")
# elif os.path.isfile('/usr/bin'):
#     print("\nIt is a normal file")
# else:
#     print("It is a special file (socket, FIFO, device file)" )
# print()


#current file path
# import os
# print(os.path.abspath(__file__) )
# print(os.path.abspath("profileimage.jpeg") )
#
# print(os.path.realpath(__file__))
#
# #absolute path
#
# from pathlib import Path
#
# print(Path("profileimage.jpeg").resolve())
# print(Path("python3.6").resolve())
# print(Path("python3.6").resolve()

# 86. Write a Python program to get the ASCII value of a character.

# print(ord("w"))
# print(ord("W"))

#87. Write a Python program to get the size of a file.

# import os
# x=(os.path.getsize('/usr/bin'))
# print('%dB'%x)


#88. Given variables x=30 and y=20, write a Python program to print t "30+20=50"

# x=30
# y=20
#
# print("30+20=%d"%(x+y))
# print("%d+%d=%d" %(x,y,x+y))

#89. Write a Python program to perform an action if a condition is true.

# x=1
#
# if x == 1:
#     print("\nFirst day of a Month!")
# else:
#     pass

#90. Write a Python program to create a copy of its own source code.


# print((lambda str='print(lambda str=%r: (str %% str))()': (str % str))())
# print( open(__file__).read())

# 91. Write a Python program to create a copy of its own source code.

#1

# z=500
# x=200
# #1
# z=z+x #700
# x=z-x #500
# z=z-x #200
# print(z)
# print(x)

#2

# print("\nBefore swap x=%d, and z=%d"%(x,z))
# z,x=x,z
# print("\nAfter  swap x=%d, and z=%d"%(x,z))

# 92. Write a Python program to define a string
# containing special characters in various forms.


# print("/"'![]{}'"$%^&*()")
# print(r"""$"'\n'"@~#""")
# print(r'"\"/^&*()"|"\$/')


#93. Write a Python program to get the identity of an object
# x=['slow','fast','medium']
# print(id(x))
#
# adress=id(x)
# print(adress)

#94. Write a Python program to convert a byte string to a list of integers.

# decode_into_str=b''.decode('utf-8')
#
#
# code = bytes([231, 131])
# code       # b'\xe7\x83'
# type(code) # <class 'bytes'>
# list(code) # [231, 131]
#
# string ="Write a Python program to convert a byte string to a list of integers."
# byt=list(bytes(string,'utf-8'))
# print(*byt ,sep = "\n")

# 95. Write a Python program to check if a string is numeric.

# def check_list(x):
#     try:
#         float(x)
#         print (True)
#     except ValueError:
#         print(False)
# x="wlaskksaa"
# x="wteuu3444l"
# x="3444"

# check_list(x)

# 96. Write a Python program to print the current call stack.
# import traceback
# def f1():
#     return abc()
# def abc():
#     traceback.print_stack()
# f1()
# print()
#
# PycharmProjects/Training-session


# import os
# print(os.path.abspath(__file__) )

#97. Write a Python program to list the special variables used within the language.

# s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
# print()
# print( '\n'.join(','.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )
# print()

# error=[ArithmeticError,AssertionError,AttributeError,BaseException,BlockingIOError,BrokenPipeError,BufferError,BytesWarning
# ChildProcessError,ConnectionAbortedError,ConnectionError,ConnectionRefusedError,ConnectionResetError,DeprecationWarning,EOFError,Ellipsis
# EnvironmentError,Exception,False,FileExistsError,FileNotFoundError,FloatingPointError,FutureWarning,GeneratorExit
# IOError,ImportError,ImportWarning,IndentationError,IndexError,InterruptedError,IsADirectoryError,KeyError
# KeyboardInterrupt,LookupError,MemoryError,ModuleNotFoundError,NameError,None,NotADirectoryError,NotImplemented
# NotImplementedError,OSError,OverflowError,PendingDeprecationWarning,PermissionError,ProcessLookupError,RecursionError,ReferenceError
# ResourceWarning,RuntimeError,RuntimeWarning,StopAsyncIteration,StopIteration,SyntaxError,SyntaxWarning,SystemError
# SystemExit,TabError,TimeoutError,True,TypeError,UnboundLocalError,UnicodeDecodeError,UnicodeEncodeError
# UnicodeError,UnicodeTranslateError,UnicodeWarning,UserWarning,ValueError,Warning,ZeroDivisionError]
#
# special1=[__annotations__,
# __build_class__,__builtins__,__cached__,__debug__,__doc__,__file__,__import__,__loader__
# __name__,__package__,__spec__]
#
# special2=[abs,all,any,ascii,bin
# bool,bytearray,bytes,callable,chr,classmethod,compile,complex,
# copyright,credits,delattr,dict,dir,divmod,enumerate,eval,
# exec,exit,filter,float,format,frozenset,getattr,globals,
# hasattr,hash,help,hex,id,input,int,isinstance,
# issubclass,iter,len,license,list,locals,map,max,
# memoryview,min,next,object,oct,open,ord,pow,
# print,property,quit,range,repr,reversed,round,set,
# setattr,slice,sorted,staticmethod,str,sum,super,tuple]

#98. Write a Python program to get the system time.

#1 import time
#print(time.ctime())

#2
#import datetime
#print(datetime.datetime.now().time())

#99. Write a Python program to clear the screen or terminal.
import os
import time
os.system("clear")
def wind_cleare():
    os.system("cls")
    return
#
# import os
# import time
# # for windows
# # os.system('cls')
# os.system("ls")
# time.sleep(2)
# # Ubuntu version 10.10
# os.system('clear')

print(os.path.abspath("PycharmProjects/Training-session/Exercises , Basic Part 1.py"))


