# 1. Write a Python program to convert kilometers to miles?

km = int(input("Enter the value in kilometers: "))
# 1 Kilometre = 0.621371 Mile
r = 0.621371
# Converting km to miles.
miles = km * r
print("The entered value in Miles: ", miles)


# 2. Write a Python program to convert Celsius to Fahrenheit?

c = int(input("Enter temp in celcius: ")) 
# Converting the temperature to fehrenheit 
f = (c * 1.8) + 32
print("Temp in fehrenhite is:",f)


# 3. Write a Python program to display calendar?

import calendar
yy = 2022
print(calendar.calendar(yy))

# for given month in a year
import calendar 
yy = 2023
mm = 1
print(calendar.month(yy, mm))


# 4. Write a Python program to solve quadratic equation?
 
import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
# calculate the discriminant  
d = (b**2) - (4*a*c)  
  
# find two solutions  
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  
print('The solution are {0} and {1}'.format(sol1,sol2))   


# 5. Write a Python program to swap two variables without temp variable?

x = 54
y = 75
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
x, y = y, x
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)
