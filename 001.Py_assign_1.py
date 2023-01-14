#!/usr/bin/env python
# coding: utf-8

# # Assignment_1

# ## Questions

# In[2]:


# 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# * 
# 'hello'
# -87.8
# - 
# / 
# +	
# 6 

# 2. What is the difference between string and variable?

# 3. Describe three different data types.

# 4. What is an expression made up of? What do all expressions do?

# 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?

# 6. After running the following code, what does the variable bacon contain?
# bacon = 22
# bacon + 1

# 7. What should the values of the following two terms be?
# 'spam' + 'spamspam'
# 'spam' * 3

# 8. Why is eggs a valid variable name while 100 is invalid?

# 9. What three functions can be used to get the integer, floating-point number, or string version of a value?

# 10. Why does this expression cause an error? How can you fix it?
# 'I have eaten ' + 99 + ' burritos.'


# ## Answers

# In[ ]:


# Ans.1
"""
* is an Expression which is a mathematical operator used for multiplication
'hello' is a string value
-87.8 is a floating point value
- is an Expression which is a mathematical operator used for subtaction
/ is an Expression which is a mathematical operator used for division
+ is an Expression which is a mathematical operator used for addition
6 is an integer value
"""


# In[ ]:


# Ans.2
"""
A string is like a english word or sentence which is surrounded by either single or double quotation marks.
For eg: 'Hello, My name is Hardik'.

A variable is like a containe which is used for storing values.
For eg: a = 'Hello world'. in this eg, a is a variable.
"""


# In[ ]:


# ans.3
"""
There are many data types in python language. Some of them are string, integer, float, 
bool, complex, list, tuple , dictionary etc.

1. int data type: It is a whole no which can be positive or negative and of unlimited length. eg: 851561 is an int
2. bool data type: When we compare two value we get the ans in bool type i.e True or False
3. list data type: It is used to store multiple items/diff data types in a single variable using [] brackets. 
eg: [2,3.6,8,'Hello',True,9+5j]
"""


# In[ ]:


# Ans.4
"""
An Expression is a combination of operators and operands which is used to give us some values by using them.
There are many expressions or operators in python which are used to perform some mathemaical operations just like adition,
subtraction, multiplication, division, modulus etc.
"""


# In[ ]:


# Ans.5
"""
In Expression, we can print or assign a value to a variable while we can't do anything like this in a statement.
Example for expressions: spam = 10, 2+3, 'Hardik', max(85,63), True, None etc.
Example for a statement: If-else condition, elif condition, for loop, while loop, break statement, continue etc.
"""


# In[4]:


# Ans.6
bacon = 22


# In[5]:


bacon+1


# In[9]:


bacon
# No change in variable bacon


# In[10]:


# Ans.7
'spam' + 'spamspam'


# In[11]:


#Ans.7
'spam' * 3


# In[ ]:


# Ans.8
"""
Eggs is a valid variable name because a variable name can start with a letter 
100 is an invalid variable name because a variable name can't start with a number
"""


# In[ ]:


# Ans.9
"""
You can use int(), float() and str() functions to get the integer, float and string version of a value
"""


# In[12]:


# Ans.10
'I have eaten ' + 99 + ' burritos.'


# In[ ]:


"""It is showing us error because we cannot concatenate string and integer values """


# In[13]:


# Now, This code will run
'I have eaten ' + '99' + ' burritos.'

