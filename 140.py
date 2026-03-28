# 1 -  Write a Python program to print "Hello Python"
print('Hello World.')


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 2 -  Write a Python program to do arithmetical operations addition and division
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
sum = num1 + num2 
print('Sum of num1 and num2 is equal to: ' + str(sum))

if num2 == 0:
    print('Error: Division is not allowed.')
else:
    div = num1/num2
    print('div of num1 and num2 is equal to: ' + str(div))



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# 3 -  Write a Pvthon program to find the area of a triangle.
base = float(input('Enter base: '))
height = float(input('Enter height: '))
triangleArea = (base * height)/2
print('The area of the triangle is ' + str(triangleArea))


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# 4 -  Write a Python program to swan two variables
a = input('Enter a: ')
b = input('Enter b: ')
print(a, b)
temp = a
a = b
b = temp
print(a, b)

a = 5
my_list = [1, 2, 3, 4, 5]
temp = a in my_list
print(temp)
# Output: True

a = 'z'
my_string = 'abcdefg'
temp = a in my_string
print(temp)
# Output: False


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# 5 -  Write a Python program to generate a random number
import random
print(random.randint(1, 100000000000))


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# 6 -  Write a Python program to convert Kilometers to miles:

x_Kilometers = float(input("Enter the distance in kilometers: "))

# We know that: 1 Kilometers = 0.621371 mile -----> we'll call the conversion_factor f 

f = 0.621371

x_miles = f * x_Kilometers 

print(str(x_Kilometers) + " km equals to " + str(x_miles) + " miles.")


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# 7 - Write a Python proaram to convert Celsius to Fahrenheit

x_celsius = float(input("Enter the temperature: "))

# (0C * 9/5) +32 = 32F

x_Fara = (x_celsius * 9/5) + 32

print(str(x_celsius) + " is " + str(x_Fara) + " Fahrenheit.")


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 8 - Write a Puthon program to displav calendar.

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

cal = calendar.month(year, month)
print(cal)




# Write a Python program to display calendar with the exact date =========
#========== NOT CORRECT ===========
import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

cal = calendar.month(year, month, day)
print(cal)





#========== This is correct ==============
import datetime

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

date = datetime.date(year, month, day)
print(date.strftime("%A"))  # prints the day of the week






#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 9 - Write a Python program to solve quadratic equation.







#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 10 - Write a Python program to swan two variables without temp variable.

var1 = int(input("Enter year: "))
var2 = int(input("Enter year: "))

print("var1 = "+ str(var2))
print("var1 = "+ str(var1))


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 11 - Write a Python Program to Check if a Num is Positive. Negative or Zero

C = int(input ("enter a number: "))
if C > 0:
    print("C is positive.")
elif C < 0:
    print("C is negative.")
else:
    print("C is equal to zero..")






#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#12 - Write a Python Program to Check if a Number is Odd or Even

C = int(input ("enter a number: "))
if C%2 == 0:
    print("C is even")
else:
    print("C is odd")



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#13 - Write a Python Program to Check Leap Year.

year = int(input("Enter  year: "))
if year%400 == 0 and year%100 == 0:
    print(str(year) + " is a leap year.")
elif year%4 == 0 and year%100 != 0:
    print(str(year) + " is a leap year.")
else:
    print(str(year) + " is a NOT a leap year.")



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#14 - Write a Python Program to Check Prime Number.







#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#15 - Write a Python Program to Print all Prime Numbers in an Interval of 1.10










#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# 16 - Write a Pvthon Program to Find the Factorial of a Number.








#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 17 - Write a Puthon Program to Displav the multiplication Table









#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 18 - Write a Python Program to Print the Fibonacci sequence 









#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 19 - Write a Python Program to Check Armstrong Number?








