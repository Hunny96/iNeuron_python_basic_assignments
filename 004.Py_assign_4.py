# Q1. What exactly is []?

It is an empty list which has no items in it. 


#  Q2. In a list of values stored in a variable called spam, how would you assign the value 'hello'; as the third value? (Assume [2, 4, 6, 8, 10] are in spam.) 

spam = [2,4,6,8,10]
spam[2] = "hello"
print(spam)
now spam has [2,4,'hello',8,10]


# Let's pretend the spam includes the list ['a','b','c','d'] for the next three queries.

# Q3. What is the value of spam[int(int('3'*2)/11)]?

spam = ['a','b','c','d']

s = int('3'*2) # it will give us 33

int(s/11) # then it will give us the integer value 3

Therefor, spam[int(int('3'*2)/11)] = spam[3] which will be d 
spam[3] = d

# Q4. What is the value of spam[-1]?

spam[-1] = d 


# Q5. What is the value of spam[:2]?

spam[:2] = ['a','b'] 

# # Let's pretend bacon has the list [3.14, 'cat', 11, 'cat', True] for the next three questions.

bacon = [3.14, 'cat', 11, 'cat', True]

#  Q6. What is the value of bacon.index('cat')?

bacon.index('cat') = 1


# Q7. How does bacon.append(99) change the look of the list value in bacon?

bacon.append(99)
#  new list will be [3.14, 'cat', 11, 'cat', True, 99]


# Q8. How does bacon.remove('cat') change the look of the list in bacon?

bacon.remove('cat')
# new list will be [3.14, 11, 'cat', True, 99]


# Q9. What are the list concatenation and list replication operators?

'+' is called as list concatenation operator. It is used to concatenate the list 
'*' is called as list replication operator. It is used to replicate or copy the list


# Q10. What is difference between the list methods append() and insert()?

'append()' method is used to append or add any item to the end of a list. it's syntax is list.append()
'insert()' method is used to add any item where-ever you want to add by using index number. it's syntax is list.insert(index no, item) 


# Q11. What are the two methods for removing items from a list?

del and remove() are the two methods for removing items from a list


# Q12. Describe how list values and string values are identical.

Both list and string have len() function to count the no of items or characters. They both have slicing and indexing methods. 
They both can be concatenated and replicated by using '+' and '*' operator. They both have built-in 'in' and 'not in' method to find the element in them. 
They both can be used in 'for' loop


# Q13. What&#39;s the difference between tuples and lists?

Lists are mutable data type in python which means that we can add, remove or change any item inside it. lists use the square brackets '[]'
Tuples are immutable data type in python language. We can not add, remove or change any item in it. Tuples are written using '()' parenthesis


# Q14. How do you type a tuple value that only contains the integer 42?

It can be written as (42)


# Q15. How do you get a list value&#39;s tuple form? How do you get a tuple value&#39;s list form?

To convert a list into tuple, we use tuple() function and to convert a tuple into list, we use list() function
example:
# convert list into tuple
l = [1,5,9,3.25,True]
t1 = tuple(l)
print(l)
print("Tuple form of l is:",t1)
print("----")

# convert a tuple into list
t = ("Hardik",86,7,3.6,False)
print(t)
l1 = list(t)
print("List form of t is:",l1)


# Q16. Variables that &quot;contain&quot; list values are not necessarily lists themselves. Instead, what do they contain?

Variables will contain references to list values rather than list values themselves.


# Q17. How do you distinguish between copy.copy() and copy.deepcopy()?

The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list. 
That is, only copy.deepcopy() will duplicate any lists inside the list.
