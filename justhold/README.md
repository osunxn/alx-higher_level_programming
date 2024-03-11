" 0x05. Python - Exceptions

## Description

This repository contains solutions to the "0x05. Python - Exceptions" tasks. The project explores Python programming, focusing on errors and exceptions. The tasks cover various aspects, including handling exceptions, safe printing, division, and more.

## Learning Objectives

By completing this project, you are expected to:

- Understand why Python programming is advantageous.
- Differentiate between errors and exceptions.
- Comprehend what exceptions are and how to use them.
- Learn when and how to handle exceptions properly.
- Explore the purpose of catching exceptions.
- Understand how to raise a built-in exception.
- Know when to implement a clean-up action after an exception.

## Requirements

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- Files should end with a new line.
- The first line of all files should be `#!/usr/bin/python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code should follow PEP 8 style guidelines (`pycodestyle` version 2.8.*).
- All files must be executable.
- The length of files will be tested using `wc`.

## Tasks

### 0. Safe list printing

Write a function `safe_print_list(my_list=[], x=0)` that prints `x` elements of a list.

### 1. Safe printing of an integers list

Write a function `safe_print_integer(value)` that prints an integer with "{:d}".format().

### 2. Print and count integers

Write a function `safe_print_list_integers(my_list=[], x=0)` that prints the first `x` elements of a list and only integers.

### 3. Integers division with debug

Write a function `safe_print_division(a, b)` that divides two integers and prints the result.

### 4. Divide a list

Write a function `list_division(my_list_1, my_list_2, list_length)` that divides element by element two lists.

### 5. Raise exception

Write a function `raise_exception()` that raises a type exception.

### 6. Raise a message

Write a function `raise_exception_msg(message="")` that raises a name exception with a message.

### 7. Safe integer print with error message

Write a function `safe_print_integer_err(value)` that prints an integer and returns True if the value has been correctly printed, otherwise, returns False and prints in stderr the error preceded by "Exception:".

### 8. Safe function

Write a function `safe_function(fct, *args)` that executes a function safely.

### 9. ByteCode -> Python #4

Write the Python function `def magic_calculation(a, b)` that does exactly the same as the provided Python bytecode.

### 10. CPython #2: PyFloatObject

Create three C functions that print some basic info about Python lists, Python bytes, and Python float objects.

## Testing

The project includes test scripts (`main` files) to validate the correctness of the implemented functions.
Each task hasits own test script.
