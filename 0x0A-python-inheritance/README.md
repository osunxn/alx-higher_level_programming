# README.md

## 0x0A. Python - Inheritance

### Overview

This project focuses on the concept of inheritance in Python, exploring how classes can inherit attributes and methods from other classes. The primary goal is to understand the fundamentals of object-oriented programming (OOP) and inheritance within the context of the Python programming language.

  - Notes
All your files should end with a new line.
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
Your code should use the pycodestyle (version 2.8.) style (version 2.7. for global variable names).
We strongly encourage you to work together on test cases, so that you don’t miss any edge case.
We strongly encourage you to ask questions to your peers and fellow students, in case of a doubt.

### Learning Objectives

Upon completion of this project, you should be able to explain the following concepts without relying on external sources:

1. **General**
   - Why Python programming is awesome
   - Understanding of superclass, base class, or parent class
   - What a subclass is
   - Listing all attributes and methods of a class or instance
   - Adding new attributes to an instance
   - Inheriting a class from another
   - Defining a class with multiple base classes
   - The default class every class inherits from
   - Overriding a method or attribute inherited from the base class
   - Attributes or methods available by heritage to subclasses
   - The purpose of inheritance
   - How to use `isinstance`, `issubclass`, `type`, and `super` built-in functions

### Resources

Read or watch the following resources to enhance your understanding:

- [Inheritance](https://docs.python.org/3/tutorial/errors.html)
- [Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
- [Inheritance in Python](https://www.geeksforgeeks.org/inheritance-in-python/)
- [Learn to Program 10: Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)

### Requirements

#### Python Scripts

- **Allowed Editors:** vi, vim, emacs
- **Interpretation/Compilation:** Ubuntu 20.04 LTS using Python 3 (version 3.8.5)
- **File Endings:** All files should end with a new line
- **Shebang:** The first line of all files should be exactly `#!/usr/bin/python3`
- **README.md:** A mandatory file at the root of the project folder
- **Code Style:** Your code should use the `pycodestyle` (version 2.8.*)
- **Executability:** All your files must be executable
- **Length Verification:** The length of your files will be tested using `wc`

#### Python Test Cases

- **Allowed Editors:** vi, vim, emacs
- **File Endings:** All your test files should end with a new line
- **Test Folder:** All your test files should be inside a folder named `tests`
- **Test File Format:** All your test files should be text files with the extension `.txt`
- **Execution:** All your tests should be executed using the command: `python3 -m doctest ./tests/*`
- **Documentation:** All your modules, classes, and functions should have documentation

#### Documentation

- **Comments:** Do not use the words `import` or `from` inside your comments
- **Quiz Questions:** Complete the quiz questions successfully

### Tasks

#### 0. Lookup

Write a function that returns the list of available attributes and methods of an object:

```python
def lookup(obj):
    """
    Returns a list object
    """
1. My list
Write a class MyList that inherits from list:

python

class MyList(list):
    """
    Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
    """
2. Exact same object
Write a function that returns True if the object is exactly an instance of the specified class; otherwise False:

python

def is_same_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class; otherwise, False
    """
3. Same class or inherit from
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False:

python

def is_kind_of_class(obj, a_class):
    """
    Returns True if obj comes from a_class or a class that inherited from a_class; otherwise, False
    """
4. Only sub class of
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False:

python

def inherits_from(obj, a_class):
    """
    Returns True if obj inherited from a_class or a class that inherited from a_class; otherwise, False
    """
5. Geometry module
Write an empty class BaseGeometry:

python

class BaseGeometry:
    """
    Empty class BaseGeometry
    """
6. Improve Geometry
Write a class BaseGeometry with a public instance method area(self) that raises an Exception with the message area() is not implemented:

python

class BaseGeometry:
    """
    Class BaseGeometry with method area() that raises an Exception
    """
7. Integer validator
Write a class BaseGeometry with a public instance method integer_validator(self, name, value) that validates value:

python

class BaseGeometry:
    """
    Class BaseGeometry with method integer_validator() for value validation
    """
8. Rectangle
Write a class Rectangle that inherits from BaseGeometry:

python

class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry
    """
9. Full rectangle
Write a class Rectangle that inherits from BaseGeometry with instantiation requirements:

python

class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry with instantiation requirements
    """
10. Square #1
Write a class Square that inherits from Rectangle:

python

class Square(Rectangle):
    """
    Class Square that inherits from Rectangle
    """
11. Square #2
Write a class Square that inherits from Rectangle:

python

class Square(Rectangle):
    """
    Class Square that inherits from Rectangle
    """
12. My integer
Write a class MyInt that inherits from int:

python

class MyInt(int):
    """
    Class MyInt that has == and != operators inverted
    """
13. Can I?
Write a function that adds a new attribute to an object if it’s possible:

python

def add_attribute(obj, name, value):
    """
    Raises a TypeError exception if the object can’t have a new attribute
    """
