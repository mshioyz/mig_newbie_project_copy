# HW0: A very basic introduction to Python.
#  
# Python is a goated interpreted, high level, and 
# dynamically typed* (it can be static too) language. 
# What this means: it doesn't compile into an executable 
# but the Python interpreter evaluates the output of some
# Python code and spits that bad boy out. It's incredibly 
# high level because... it's almost english. e.g: "if 
# element in _list: return True" is valid Python code. So
# Pythonic. It's also dynamically typed: in c++ you'd write
# "std::vector<int> v;" to create a vector/list of type int,
# but in Python you'd just write "_list = []", without
# specifying its type at instantiation. Python just gets it! 
# So Pythonic. 
#
# These elements make it fantastic for interviews (super easy to write)
# and great for fast iteration in the biz (see Akuna and HRT python dev).
# 
# Python3 is probably the dominant version of Python, 
# so make sure when you install python, you get Python3.
# 
# FAQ: 
# What I am doing on this HW? Fill out the functions with TODO!
# How do I install Python? Find the relevant binary for your dev env and install! 
# If you're on a unix based system, you can probably just use your package manager. 
# If you're having trouble running Python after the install, check your path. 
# How do I run a Python script? "python <filename>.py" or "python3 <filename>.py"!
# How do I do x in Python? Refer to google, geeksforgeeks, etc!   
# I love pointers! Are there pointer in Python? Everything is a reference unfortunately...
# Pointers don't really exist in Python. 
# 
# The inclusive of the FAQ is to not discourage question, feel free to ask any questions 
# about the homework after spending some time googling and hacking at it.
# If you have yet to take 281, some of the data structures might 
# be foreign and that's a-okay. Google their basic functionality, no need to get into 
# the nitty gritty underlying implementation (unless you want to) and once again feel 
# free to ask questions.

# TODO: Return "Positive", "Negative", or "Zero", conditioned on the given param.
def classify_number(n):
    # Basic Conditionals: Using if-elif-else to handle multiple conditions.
    pass # Delete me when you fill this function out
# Recall that Python can be statically typed too - 
# this is an example of the above function, statically typed.
# def classify_number(n: int) -> str: 
#     pass

# Tests
assert classify_number(10) == "Positive"
assert classify_number(-1) == "Negative"
assert classify_number(0) == "Zero"

# TODO: Return "Even" or "Odd", conditioned on the given param using a ternary operator   
def even_or_odd(n):
    # Ternary Operator: Condensed if-else for simple evaluations.
    pass
# Tests
assert even_or_odd(4) == "Even"
assert even_or_odd(3) == "Odd"

# TODO: Return the sum of the integers from 0-n using the range function (No math here outside of basic arithmetic!)
def sum_to_n(n):
    # For Loops and the Range Function: Iterating over a sequence of numbers.    
    pass
# Tests
assert sum_to_n(5) == 15
assert sum_to_n(100) == 5050

# TODO: given a string of lowercase alphabetical characters, return a list of integers corresponding to 
# each characters' position in the alphabet. Refer to the test for an example.
def character_indexes(string):
    # Python strings: working with strings
    pass
assert character_indexes("abcd") == [0,1,2,3]
    
# TODO: Given a list of numbers, return a list of with each of those numbers doubled 
def double_numbers(numbers):
    # Lists: Working with mutable sequences of data.
    pass
# Tests
assert double_numbers([1, 2, 3]) == [2, 4, 6]
assert double_numbers([]) == []

# TODO: Given a list of tuples, sort the list on the second element of each tuple, ascending order 
def sort_by_second(tuple_list):
    # Sorts, Lambda Sorts: Sorting based on custom criteria.
    pass    
# Tests
assert sort_by_second([(1, 2), (3, 1), (5, 0)]) == [(5, 0), (3, 1), (1, 2)]

# TODO: Return a list of unique elements, sorted. 
def unique_sorted(elements):
    # Sets: Removing duplicates and performing set operations.
    pass
# Tests
assert unique_sorted([3, 1, 2, 3, 4, 2]) == [1, 2, 3, 4]

# TODO: Return a dictionary that maps each character in the string to its frequency.
def character_count_dict(string):
    # Dict: hashtable equivalent. Consider also using a collections.defaultdict - play around with the two!
    pass
# Tests
assert character_count_dict("hello") == {"h": 1, "e": 1, "l": 2, "o": 1} 

# TODO: Return a counter object that maps each character in the string to its frequency.
from collections import Counter
def character_count(string):
    # Counter: Specialized dictionary for counting hashable objects.
    pass
# Tests
assert character_count("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}

# TODO: Given a deque, efficiently append element to the left and right of the deque.
from collections import deque
def add_to_ends(element, d):
    # Collections.deque: Generalizes a queue and a stack; efficient appends and pops from both ends.
    pass
# Tests
d = deque([2, 3, 4])
assert add_to_ends(1, d) == deque([1, 2, 3, 4, 1])

# TODO: Implement the fibonacci function for a demonstration below:
def fib(n):
    pass
    
def sum_fib(n):
    sum = 0
    for i in range(n):
        sum += fib(i)
    return sum 

# A more advanced feature: intentioned caching! good for optimizing
# "overlapping" calls (DP) to the function.
# It does memoization for you! 

from functools import lru_cache
@lru_cache(maxsize=1001)
def fib_cached(n):
    # TODO: Implement me like a normal fib function.
    pass

def sum_fib_cached(n):
    sum = 0
    for i in range(n):
        sum += fib_cached(i)
    return sum 

import time
def report_fib_time():
    start_time = time.time(); sum_fib(35); end_time = time.time()
    print(f"sum_fib: ", (end_time - start_time)) 

    start_time = time.time(); sum_fib_cached(35); end_time = time.time()
    print(f"sum_fib_cached: ", (end_time - start_time)) 

report_fib_time()

# Python class demo:
class Node:
    # The self keyword is functionally* analogous to the this keyword in c++.
    def __init__(self, val=0, next=None ):
        # The above syntax for the params means "param=default_value". 
        self.val = val
        self.next = next

# Class inheritance.
class DLNode(Node):
    def __init__(self, val=0, next=None, prev=Node ):
        # Calling the super constructor
        super.__init__(self, val, next)
        self.prev = prev      

# Singly linked list in Python demo:
class LL:
    def __init__(self):
        self.head = Node(-1) # Sentinel node
    def appendleft(self, node):
        node.next = self.head
        self.head = node

# Afterword:
# Once again, you are greatly encouraged to "learn" Python for interviews.
# I say learned because Python is so beautiful it doesn't feel like learning.
# I personally believe that Python was the language spoken around the construction 
# of tower of babel - in that it's universal, beautiful, and elegant. Please
# feel free to ask questions about Python, the homework, etc.
