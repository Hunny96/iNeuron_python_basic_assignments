# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

a = int(input("Enter a: "))
if a > 0:
    print("Positive")
elif a == 0:
    print("Zero")
else:
    print("Negative")


# 2. Write a Python Program to Check if a Number is Odd or Even?

a = int(input("Enter a: "))
if a % 2 == 0:
    print("Even")
else:
    print("odd")


# 3. Write a Python Program to Check Leap Year?

year = int(input("Enter year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print("Century leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")


# 4. Write a Python Program to Check Prime Number?

a = int(input("Enter a: "))
if a == 1:
    print("prime no")
    for i in range(2,a):
        if a % i == 0:
            print("Not a prime no")
            break
    else:
        print("prime no")


# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

lower = 1
upper = 10000

print("Numbers between", lower ,"and", upper, "are:")

for num in range(lower, upper + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
            
