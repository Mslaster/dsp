# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both tuples and lists are ordered sequences of values on which one can perform operations. However, while lists are mutable, tuples are immutable. Because of this difference, only tuples can be used for keys in dictionary, since keys must also be immutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are similar in that they both contain values that are iterable. However, while lists are mutable, sets are immutable. Therefore, while with each you can check length and check membership of a value, you cannot do anything using indexing in a set. However, one can find an item more rapidly in a set since the search function works by hashtable as opposed to iterating through an entire list. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The `lambda` function is an alternate way to call a function that it usually used only briefly. As an example, when sorting through the list:  
`fruit=['apples','Oranges','bananas','Cherries']`  
To first make all of the names lowercase, you would call this lambda on each value and then sort:  
`fruit.sort(key=lambda word: word.lower())`

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are commands to perform a specific function on all values in a list. A `map` function takes a list and creates a new one based on its rules. For example, for the following list:  
`li=[5,3,7,8,6]`
The function: `[num**2 for num in li]` would square all of the elements of the list.  
A `filter` would create a new list limited by certain criteria. So, for the following:  
`[num for num in li if num > 5]` would select only the values greater than 5.  
Similar commands can be used in constructing new sets and dictionaries.

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 Days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 Days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 Days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





