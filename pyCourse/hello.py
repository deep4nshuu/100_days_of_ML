# Chapter 1 : Strings

name = "Deepanshu"
# print(name[5])   # to get char from string
# print(len(name))  # to find len of string
# print(name.index("D"))  # to find index of part. char in string
# print(name.replace("ee", "i"))  # to replace part. char in string


# Chapter 2 : Numbers

from math import*  # to import math fn
num = -5.4
# print(3 * 4 + (6/3))  # simply calc math expression
# print(str(num) + " is my fav no") # to print no with str use str() fn
# print(round(num))


# Chapter 3 : input/output from user
# name = input("Enter name: ")
# print(name)

# small calc
num1 = input("Enter num1: ")
num2 = input("Enter num2: ")
print(num1 + num2) # this will treat num1 & 2 as string not no.
res = int(num1) + int(num2)  # to solve, use int, float like data type which distinguish it from string 
# print(res)


# Chapter 4 : List (adding bunch of diff/same val)

names = ["Deep", "Rahul", "Tanish", "aaditya"]  # creation
animal = ["Tiger", "lion"]
print(names[2:])  # to print them, here we can also give range, -idx to access from back in braces
names.extend(animal)
animal.append("Giraffe")
print(names)

# list fn : .extend() ->  to merge list, .append()-> to add ele in list, .insert(idx,el), etc

# Function and ifelse condn:

# def maxNum(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else: 
#         return num3
# print(maxNum(5,4,5))

# A fully functional calculator

# num1 = float(input("Enter first no: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second no: "))

# if op == '+':
#     print(num1 + num2)
# elif op == '-':
#     print(num1 - num2)
# elif op == '/':
#     print(num1 / num2)
# elif op == '*':
#     print(num1 * num2)
# else :
#     print("Invalid operator")


# Dictionaries(Objects) : It is a special structure in python to allows us to store info in form of key-val pair

# Syntax :  dictName = {"key" : "val" ... }  
# To access: dictName["key"] or .get("key", "can pass its val if not present in dict")

# While loop
# i = 1  
# while i <= 10:  
#     print(i)   
#     i += 1    


# For loop
friends = ['Jim', 'aren', 'Rahul']
for friend in friends:
    print(friend)
for idx in range(3,10): # for idx in range(len(friends))
    print(idx) # print(friends[idx])

# Explicit fn
# print(2**3) # means 2^3
# OR
def raise_to_pow(baseNum, powNum):
    result = 1
    for idx in range(powNum):
        result = result * baseNum
    return result

# print(raise_to_pow(4, 3))

# 2D list or grids And nested loops
grid = [
    [1,2,3],
    [4,5,6]
]
#print(grid[0][1])

# for row in grid:
#     for col in row:
#         print(col)


# Translation 
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

# print(translate(input("Enter the phrase: ")))


# try and except
# try:
#     #numb = 10/0
#     num = int(input("Enter no: "))
#     print(num)
# except ZeroDivisionError:
#     print("Divided by zero")
# except ValueError as err:
#     print(err)

# Reading files : reading command allow to read files outside python such as html,css
# It allow 4 opt(r,w(to edit info),a(to add new info),r+(to do everything))
# It allow these thing( open and close file)

# 1. reading
# employee_file = open("pyCourse/emp.txt", "r") 
# print(employee_file.read()) # to read all file
# print(employee_file.readlines()[1]) # to read line with specific idx
# use readable fn to find out file is readable or not, readline() to read one line at a time, readlines() to print in form of list
# for emp in employee_file.readlines():
#     print(emp)
# employee_file.close()

# 2. writing and appending in file
# employee_file = open("pyCourse/emp.txt", "a")
# employee_file.write("Deep - Manager") # to append new info into file
# employee_file.write("\nAbhinav - Customer care")

# when we use "w", it will override/erase all contain in file and print what add in that
# "w" also allow to create new file by adding new name where fn is added while opening file



# Module - module is a py file which we can import in our exisiting py file to use it
# import app 
# print(app.emp_name[1])


# Class and Objects
# Class defines what an entity is(it's a template) and object is actual entity(it's instance of class)

from app import Student
student1 = Student("Deepanshu", "Business", 8)
# print(student1.gpa)


# How Quiz is made
from app import Questn
quesPrompt = [
    "What are the color of Apples?\n(a) Red\n(b) Blue\n(c) Brown\n\n",
    "What are the color of Banana?\n(a) Red\n(b) Yellow\n(c) Purple\n\n",
    "What are the color of Rose?\n(a) Red\n(b) Magenta\n(c) Brown\n\n",
    "What are the color of Guava?\n(a) Green\n(b) Blue\n(c) Orange\n\n"
]
# it is a ques list containing individual ques so that we can access que prompt easily
questions = [
    Questn(quesPrompt[0], "a"),
    Questn(quesPrompt[1], "b"),
    Questn(quesPrompt[2], "a"),
    Questn(quesPrompt[3], "a")
]
def quiz(questions):
    score = 0
    for que in questions:
        response = input(que.prompt)
        if response == que.ans:
            score += 1
    # print("You got " + str(score) + "/" + str(len(questions)) + " correct")

quiz(questions)


# Inheritance - a class inheriting prop of another class without writing it again


# libraries - predefined fn and classes

# To create a list by for loop
py_list = [i for i in range(1000)]
print(py_list[5])

# To now data type of value use this:
# type()

# What is the difference b/w multi-dim list and multi-dim np arr
# multi-dim list -> a list inside list


# Difference b/w List and Array
# List -> Built-in d.s store multiple vals, Store different data types, No import needed
# Array -> A d.s to store SAME Datatypes vals, Uses by importing Numpy


