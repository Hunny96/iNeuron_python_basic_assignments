#!/usr/bin/env python
# coding: utf-8

# # Questions

# In[1]:


# 1.What are the two values of the Boolean data type? How do you write them?

# 2. What are the three different types of Boolean operators?

# 3. Make a list of each Boolean operator&#39;s truth tables (i.e. every possible combination of Boolean
# values for the operator and what it evaluate ).

# 4. What are the values of the following expressions?
# (5 &gt; 4) and (3 == 5)
# not (5 &gt; 4)
# (5 &gt; 4) or (3 == 5)
# not ((5 &gt; 4) or (3 == 5))
# (True and True) and (True == False)
# (not False) or (not True)

# 5. What are the six comparison operators?

# 6. How do you tell the difference between the equal to and assignment operators?Describe a
# condition and when you would use one.

# 7. Identify the three blocks in this code:
# spam = 0
# if spam == 10:
# print(&#39;eggs&#39;)
# if spam &gt; 5:
# print(&#39;bacon&#39;)
# else:
# print(&#39;ham&#39;)
# print(&#39;spam&#39;)
# print(&#39;spam&#39;)

# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
# Greetings! if anything else is stored in spam.

# 9.If your programme is stuck in an endless loop, what keys you’ll press?

# 10. How can you tell the difference between break and continue?

# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
# program that prints the numbers 1 to 10 using a while loop.

# 13. If you had a function named bacon() inside a module named spam, how would you call it after
# importing spam?


# # Answers

# In[ ]:


# ans.1
"""
There are 2 values of Boolean data type i.e true and false.
We write them as True and False
"""


# In[ ]:


# ans.2
"""
The 3 different types of bool operators are: And, Or and Not
"""


# In[ ]:


# ans.3
"""
Truth tables of boolean operators: 

Boolean 'OR' Operator
The Boolean or operator returns True if any one of the inputs is True else returns False.

A       B       A or B
True   True     True
True   False    True
False  True     True
False  False    False


Boolean 'And' Operator
The Boolean and operator returns False if any one of the inputs is False else returns True.

A       B       A and B
True   True     True
True   False    False
False  True     False
False  False    False


Boolean 'Not' Operator
The Boolean Not operator only require one argument and returns the negation of the argument i.e. returns the True for False and False for True.

A      Not A
True   False
False  True
"""


# In[26]:


# ans.4
(5 > 4) and (3 == 5)
"""
False
"""


# In[3]:


# ans.4
"""
 False
"""
not (5 > 4)


# In[4]:


# ans.4
"""
True
"""
(5 > 4) or (3 == 5)


# In[6]:


# ans.4
"""
False
"""
not ((5 > 4) or (3 == 5))


# In[7]:


# ans.4
"""
False
"""
(True and True) and (True == False)


# In[8]:


# ans.4
"""
True
"""
(not False) or (not True)


# In[ ]:


# ans.5
"""
Six comparison operators are:
'==' Equal
'!=' Not equal
'>' Greater than
'<'Less than
'>=' Greater than or equal to
'<=' Less than or equal to
"""


# In[ ]:


# ans.6

Assignment operator is denoted by '=' whereas equal to operator is denoted by '=='
for example:
number = 10. in this eg, 10 is assigned to a variable 'number' by using '=' assignment operator
3 == 3 in this example we have compare two values by using '==' equal to operator. it will gives us True as an output


# In[32]:


number = 10
print("Number =", number)


# In[33]:


3==3


# In[11]:


# ans.7
# Identify the three blocks in this code:
spam = 0
if spam == 10:       # first block of code
    print('eggs') 
if spam > 5:          # second block of code
    print('bacon') 
else:                # third block of code
    print('ham')
    print('spam')
    print('spam')


# In[15]:


# ans.8

spam = int(input())
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")


# In[ ]:


# ans.9

To end an infinite loop, we should press 'ctrl+c'


# In[29]:


# use of break
for i in range(10):
    if(i==5):
        break
    print(i)
print('Break')

#use of  continue
for i in range(10):
    if(i==5):
        print('continue')
        continue
    print(i)


# In[ ]:


# ans.10

The main diff b/w break and contine statement is that break statement is used to jump out of the loop while 
continue statement is used to skip an iteration in a loop


# In[19]:


# ans.11
# In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
for i in range(10):
    print(i)


# In[20]:


for i in range(0,10):
    print(i)


# In[21]:


for i in range(0,10,1):
    print(i)


# In[ ]:


# There is as no such diff b/w range(10), range(0,10) and range(0,10,1) in a for loop


# In[22]:


# ans.12
# print 1 to 10 using for loop
for i in range(1,11):
    print(i)


# In[24]:


# ans.12
# print 1 to 10 using while loop
i = 1
while (i<=10):
    print(i)
    i+=1


# In[ ]:


# ans.13
By using spam.bacon().

