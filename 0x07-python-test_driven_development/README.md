# 0x07. Python - Test-driven development

## Concepts
For this project, we expect you to look at this concept:

- [Never forget a test](https://docs.python.org/3/library/doctest.html)

## Background Context
Important notice on intranet checks for Python projects Starting from today:

- Based on the requirements of each task, you should always write the documentation (module(s) + function(s)) and tests first, before you actually code anything
- The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case. But not in the implementation of them!
- Don’t trust the user, always think about all possible edge cases

## Resources
Read or watch:

- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html) (until “26.2.3.7. Warnings” included)
- [doctest – Testing through documentation](https://docs.python.org/3/library/doctest.html)
- [Unit Tests in Python](https://docs.python.org/3/library/unittest.html)
- [Unittest module](https://docs.python.org/3/library/unittest.html)
- [Interactive and Non-interactive tests](https://docs.python.org/3/library/doctest.html#what-it-tests)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- Why Python programming is awesome
- What’s an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

## Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

### Python Test Cases
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or
- method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case –
- The Checker is checking for tests!

## Quiz Questions

### Tasks

### 0. Integers addition (mandatory)
Write a function that adds 2 integers.

#### Prototype: 
```python```
def add_integer(a, b=98):
a and b must be integers or floats, otherwise raise a TypeError exception with the message a must be an 
integer or b must be an integer.
a and b must be first casted to integers if they are float.
Returns an integer: the addition of a and b.
You are not allowed to import any module.
Examples:

print(add_integer(1, 2))  # Output: 3
print(add_integer(100, -2))  # Output: 98
print(add_integer(2))  # Output: 100
print(add_integer(100.3, -2))  # Output: 98
1. Divide a matrix (mandatory)
Write a function that divides all elements of a matrix.

Prototype:

def matrix_divided(matrix, div):
matrix must be a list of lists of integers or floats, otherwise raise a TypeError exception with the
message matrix must be a matrix (list of lists) of integers/floats.
Each row of the matrix must be of the same size, otherwise raise a TypeError exception with the
message Each row of the matrix must have the same size.
div must be a number (integer or float), otherwise raise a TypeError exception with the message div must be a number.
div can’t be equal to 0, otherwise raise a ZeroDivisionError exception with the message division by zero.
All elements of the matrix should be divided by div, rounded to 2 decimal places.
Returns a new matrix.
You are not allowed to import any module.
Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
# Output: [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

2. Say my name (mandatory)
Write a function that prints My name is <first name> <last name>.

Prototype:

def say_my_name(first_name, last_name=""):
first_name and last_name must be strings otherwise, raise a TypeError exception with the message
first_name must be a string or last_name must be a string.
You are not allowed to import any module.
Examples:

say_my_name("John", "Smith")
# Output: My name is John Smith
say_my_name("Walter", "White")
# Output: My name is Walter White
say_my_name("Bob")
# Output: My name is Bob

3. Print square (mandatory)
Write a function that prints a square with the character #.

Prototype:

def print_square(size):
size is the size length of the square.
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer.
If size is less than 0, raise a ValueError exception with the message size must be >= 0.
If size is a float and is less than 0, raise a TypeError exception with the message size must be an integer.
You are not allowed to import any module.
Example:

print_square(4)

# Output:
# ####
# ####
# ####
# ####

4. Text indentation (mandatory)
Write a function that prints a text with 2 new lines after each of these characters: ., ?, and :.

Prototype:

def text_indentation(text):
text must be a string, otherwise raise a TypeError exception with the message text must be a string.
There should be no space at the beginning or at the end of each printed line.
You are not allowed to import any module.
Example:

text_indentation("This is a simple text. With some lines. And some more.")
# Output:
# This is a simple text.
# With some lines.
# And some more.

5. Max integer - Unittest (mandatory)
Since the beginning, you have been creating “Interactive tests.” For this exercise, you will add Unittests.

In this task, you will write unittests for the function def max_integer(list=[]):.

Your test file should be inside a folder tests.
You have to use the unittest module.
Your test file should be python files (extension: .py).
Your test file should be executed by using this command: python3 -m unittest tests.6-max_integer_test
All tests you make must be passable by the function below.
We strongly encourage you to work together on test cases, so that you don’t miss any edge case.


def max_integer(list=[]):
    """
    Function to find and return the max integer in a list of integers
    If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
Examples:

print(max_integer([1, 2, 3, 4]))  # Output: 4
print(max_integer([1, 3, 4, 2]))  # Output: 4

6. Matrix multiplication (advanced)
Write a function that multiplies 2 matrices.

Read: Matrix multiplication - only Matrix product (two matrices)

Prototype:

def matrix_mul(m_a, m_b):
m_a and m_b must be validated with these requirements in this order:
m_a and m_b must be a list of lists of integers or floats:
if m_a or m_b is not a list: raise a TypeError exception with the message m_a must be a list or m_b must be a list
if m_a or m_b is not a list of lists: raise a TypeError exception with the message m_a must be a list of lists or 
m_b must be a list of lists
if m_a or m_b is empty (it means: = [] or = [[]]): raise a ValueError exception with the message m_a can't be empty or 
m_b can't be empty
if one element of those list of lists is not an integer or a float: raise a TypeError exception with the message 
m_a should contain only integers or floats or m_b should contain only integers or floats
if m_a or m_b is not a rectangle (all ‘rows’ should be of the same size): raise a TypeError exception 
with the message each row of m_a must be of the same size or each row of m_b must be of the same size
If m_a and m_b can’t be multiplied: raise a ValueError exception with the message m_a and m_b can't be multiplied
You are not allowed to import any module.
Example:

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
# Output: [[7, 10], [15, 22]]

7. Lazy matrix multiplication (advanced)
Write a function that multiplies 2 matrices by using the module NumPy.

To install it: pip3 install numpy==1.15.0

Prototype:
def lazy_matrix_mul(m_a, m_b):
Test cases should be the same as 100-matrix_mul but with new exception type/message
Example:

print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

8. CPython #3: Python Strings
Create a function that prints Python strings.
Prototype: void print_python_string(PyObject *p);
Format output as specified in the prompt
Print an error message for invalid strings
Use C standard library
Compile with the provided command line

