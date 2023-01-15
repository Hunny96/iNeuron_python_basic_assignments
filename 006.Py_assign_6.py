#!/usr/bin/env python
# coding: utf-8

# 1. What are escape characters, and how do you use them?

# Escape sequences allow you to include special characters in strings. To do this, simply add a backslash (\\) before the character you want to escape.
# 
# example:
# 
# s = 'Hey, what\\'s up?'
# 
# 
# print(s)

# 2. What do the escape characters n and t stand for?

# \\n stands for new line
# 
# \\t stands for tab

# 3. What is the way to include backslash characters in a string?

# Buy using '\\\\' character

# 4. The string &quot;Howl&#39;s Moving Castle&quot; is a correct value. Why isn&#39;t the single quote character in the
# word Howl&#39;s not escaped a problem?

# Because we have used double quotes (" ") to mark the beginning and end of the string

# 5. How do you write a string of newlines if you don&#39;t want to use the n character?

# By using multiline strings(""" """)

# 6. What are the values of the given expressions?
# 
# &#39;Hello, world!&#39;[1]
# 
# 
# &#39;Hello, world!&#39;[0:5]
# 
# 
# &#39;Hello, world!&#39;[:5]
# 
# 
# &#39;Hello, world!&#39;[3:]

# 'Hello, world!'[1] --> It will give 'e'

# 'Hello, world!'[0:5]--> It will give 'Hello'

# 'Hello, world!'[:5]--> It will give 'Hello'

# 'Hello, world!'[3:]--> It will give 'lo world!

# 7. What are the values of the following expressions?
# 
# &#39;Hello&#39;.upper()
# 
# 
# &#39;Hello&#39;.upper().isupper()
# 
# 
# &#39;Hello&#39;.upper().lower()

# 'Hello'.upper()--> will give 'HELLO'

# 'Hello'.upper().isupper()--> will give True

# 'Hello'.upper().lower()--> will give 'hello'

# 8. What are the values of the following expressions?
# 
# &#39;Remember, remember, the fifth of July.&#39;.split()
# 
# 
# &#39;-&#39;.join(&#39;There can only one.&#39;.split())

# 'Remember, remember, the fifth of July.'.split()--> will give ['Remember,', 'remember,', 'the', 'fifth', 'of', 'July.']

# '-'.join('There can only one.'.split())--> will give 'There-can-only-one.'

# 9. What are the methods for right-justifying, left-justifying, and centering a string?

# For right-justifying = rjust()
# 
# For left-justifying = ljust()
# 
# For centering = center()

# 10. What is the best way to remove whitespace characters from the start or end?

# By using lstrip() or rstrip(), we can remove white spaces from start or end

# In[ ]:




