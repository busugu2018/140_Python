#Write a Python program to print "Hello Python"
print('Hello World.')




#Write a Python program to do arithmetical operations addition and division
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))
sum = num1 + num2 
print('Sum of num1 and num2 is equal to: ' + str(sum))

if num2 == 0:
    print('Error: Division is not allowed.')
else:
    div = num1/num2
    print('div of num1 and num2 is equal to: ' + str(div))




#Write a Pvthon program to find the area of a triangle.
base = float(input('Enter base: '))
height = float(input('Enter height: '))
triangleArea = (base * height)/2
print('The area of the triangle is ' + str(triangleArea))




#Write a Python program to swan two variables
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




#Write a Python program to generate a random number
import random
print(random.randint(1, 100000000000))











