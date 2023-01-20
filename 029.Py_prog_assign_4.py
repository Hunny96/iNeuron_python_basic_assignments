# 1. Write a Python Program to Find the Factorial of a Number?

num = int(input("Enter number: "))
fact = 1
if num == 0:
    print("Facorial of 0 is 1")
elif num < 0:
    print("Factorial doesn't exist for number less than 0")
else:
    for i in range(1, num+1):
        fact *= i
    print("Factorial of", num, "is", fact)


# 2. Write a Python Program to Display the multiplication Table?

num = int(input("enter number: "))
print("Multiplication table of", num, "is:")
for i in range(1,11):
    print(num, "X", i, "=", num*i)


# 3. Write a Python Program to Print the Fibonacci sequence?

def fib1(n):
    a = 0
    b = 1
    output = []
    for i in range(n):
        output.append(a)
        a, b = b, a+b
    return output
fib1(10)


# 4. Write a Python Program to Check Armstrong Number?

num = int(input("Enter a Number:"))
order = len(str(num))
temp = num;
sum = 0
while(temp>0):
    digit =temp%10
    sum += digit **order
    temp = temp//10
if(sum==num):
    print("",num,"is an Armstrong number")
else:
    print("",num,"is not an Armstrong number")


# 5. Write a Python Program to Find Armstrong Number in an Interval?

lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   sum = 0  
   temp = num  
   while temp > 0:  
       digit = temp % 10  
       sum += digit ** 3  
       temp //= 10  
       if num == sum:  
            print(num)  


# 6. Write a Python Program to Find the Sum of Natural Numbers?

n=int(input("Enter a number: "))
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
print("The sum of first n natural numbers is",sum1)
