# 1. Write a Python program to print &quot;Hello Python&quot;?

print("Hello Python")


# 2. Write a Python program to do arithmetical operations addition and division.?

num1 = int(input("Enter first no: "))
num2 = int(input("Enter second no: "))

sum = num1 + num2
division = num1/num2 

print("sum of num1 and num2 is:",sum)
print("division of num1 and num2 is:",division)


# 3. Write a Python program to find the area of a triangle?

b = int(input("Enter base: "))
h = int(input("Enter height: "))

area = (b*h)/2

print("Area of triangle is:",area)


# 4. Write a Python program to swap two variables?

x = "Hardik"
y = "Manchanda"
 
temp = x
x = y
y = temp
 
print("Value of x:", x)
print("Value of y:", y)


# 5. Write a Python program to generate a random number?

import random  
n = random.randint(0,50)  
print(n)  
