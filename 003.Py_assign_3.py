#!/usr/bin/env python
# coding: utf-8

# # Q1. Why are functions advantageous to have in your programs?

The advantage of a function is to reduce the need for duplicate code. 
It will make he program shorter and easier to understand and update


# # Q2. When does the code in a function run: when it's specified or when it's called?

code in a function run when it is called


# # Q3. What statement creates a function?

The def statement creates a function


# # Q4. What is the difference between a function and a function call?

A function is a block of code that does a particular operation and returns a result.
It usually accepts inputs as parameters and returns a result. The parameters are not mandatory.
E.g:
Function add(a,b)
return a+b

A function call is the code used to pass control to a function.
E.g.:
b = add(5,6)
Now b will have the value 11.


# # Q5. How many global scopes are there in a Python program? How many local scopes?

There is one global scope, and a local scope is created whenever a function is called.


# # Q6. What happens to variables in a local scope when the function call returns?

When a function returns, the local scope gets destroyed


# # Q7. What is the concept of a return value? Is it possible to have a return value in an expression?

A return value is the value that a function call evaluates to. 
Yes it is possible to have a return value in an expression like any value.


# # Q8. If a function does not have a return statement, what is the return value of a call to that function?

It's return value will be None.


# # Q.9 How do you make a function variable refer to the global variable?

By using global statement in a function, we can make a function variable a global variable


# # Q10. What is the data type of None?

None Type


# # Q11. What does the sentence import areallyourpetsnamederic do?

This will import a module named areallyourpetsnamederic 


# # Q12. If you had a bacon() feature in a spam module, what would you call it after importing spam?

spam.bacon()


# # Q13. What can you do to save a programme from crashing if it encounters an error?

Place the line of code in a try clause.


# # Q14. What is the purpose of the try clause? What is the purpose of the except clause?

The try block lets you test a block of code for errors

The except block lets you handle the error. 

