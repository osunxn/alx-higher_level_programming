Python and C Scripts


![Alt Text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/48a9fdbd67c84a328a9df9ec8d93b9ac2458ac37721d7d53e51a27fb2bdc5263.jpg)


This repository contains a collection of Python and C scripts with their respective descriptions and usage.

Python Scripts
0. Run Python file
Description: This script runs a Python file whose name is saved in the environment variable $PYFILE.
Usage: Export the Python file name to $PYFILE and execute the script.
export PYFILE=main.py
./0-run


1. Run inline
Description: This script runs Python code stored in the environment variable $PYCODE.
Usage: Export the Python code to $PYCODE and execute the script.
export PYCODE='print(f"Best School: {88+10}")'
./1-run_inline


2. Hello, print
Description: A Python script that prints the message "Programming is like building a multilingual puzzle."
Usage: Run the script.
./2-print.py


3. Print integer
Description: This Python script prints an integer stored in the variable number, followed by "Battery street."
Usage: Run the script.
./3-print_number.py


4. Print float
Description: A Python script that prints a floating-point number stored in the variable number with a precision of 2 digits.
Usage: Run the script.
./4-print_float.py


5. Print string
Description: This Python script prints a string stored in the variable str three times, followed by its first 9 characters.
Usage: Run the script.
./5-print_string.py


6. Play with strings
Description: A Python script that prints "Welcome to Holberton School!" without using any loops or conditional statements.
Usage: Run the script.
./6-concat.py


7. Copy - Cut - Paste
Description: This script manipulates a string variable and extracts specific parts of it.
Usage: Run the script.
./7-edges.py


8. Create a new sentence
Description: This script combines parts of two strings to create a new sentence.
Usage: Run the script.
./8-concat_edges.py


9. Easter Egg
Description: A Python script that prints "The Zen of Python" by Tim Peters.
Usage: Run the script.
./9-easter_egg.py


C Scripts
10. Linked list cycle
Description: This C script checks if a singly linked list has a cycle in it.
Usage: Compile and run the script.


gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle
./cycle
The repository contains various Python and C scripts, each serving a unique purpose. Detailed usage instructions are provided for each script. Enjoy exploring and using these scripts!
