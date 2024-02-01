'''
1) Explain the concept of Dynamic Typing in Python

Dynamic typing is a fundamental concept in Python. Variables can change their data type during runtime.
Python is a dynamic-typed language where the data type of a variable is determined at the runtime rather than explicitly
declared at the compile time

2) Explain the difference between list and tuple 

Mutability: Lists are mutable, meaning you can modify their elements (add, remove, change). Tuples are immutable;
their elements cannot be changed after creation.
Syntax: Lists use square brackets […], while tuples use parentheses (…).
Performance: Tuples are generally faster and require less memory than lists.
Use Cases: Lists are suitable for collections of items that may change, while tuples are used for collections
that should remain constant.

3) How do you create a virtual env?

Using the module VENV is possible to create a virtual env
python3 -m venv <env_name>
source <env_name> activate

4) What is PEP8?

PEP8 stands for Python Enhancement Proposal and it is a style guide for Python code and it's
so important for many reasons:

Code consistency
Collaboration
Readability
Code quality

5) How do you define a function in python?

def python_function(param1, param2):

    total = param1 + param2
    return total

6) Explain the difference between local and global variable

Local variable is a variable defined within a function and it can only be accessed within the function
Global variable is a variable outside the functions and is accessible throughout the entire program

7) What are the main types in Python ?

Int (e.g. 4, 10, -5)
Str (e.g 'hello' , 'Luca')
Float (e.g. 4.5, 3.10)
List ['a', 1, 'Luca']
Tuple ('a', 1, 'Luca')
Dict {'Name':'Luca', 'Surname':'Lombardi'}
Bool Boolean Values (True or False)

8) How do you open and close a file in python?

file = open('file_name.txt', 'r') #reading
file.close

9) What is a python decorator, and how is it used?

Decorator is an outer function encompassing inner function and it is used to add functionality to functions,
such as logging, authentication, memorization.

@python_decorator
def python_function():

10) What is the purpose of '__init__ == "__main__"' ?

This statement is used to check whether a Python script is being run as the main program or if it is being imported
as a module into another script. The code inside this block will only execute if the script is run directly,
not when it is imported as a module into another script

11) Explain the concept of list comprehension

List comprehension is a coincise and readable way to create lists in Python. It allows you to generate a new list
by applying an expression to each item in a existing iterable and optionally applying a filter.

new_list = [expression for item in iterable if condition]
a = [2, 4, 6, 7]
b = ['a', 'b', 'c', 'd']
new_a = [num ** 2 for num in a if num > 4]
new_c = [(x, y) for x in a for y in b]


12) How do you handle expressions in python using try and except?

Yoy can enclose the code that might raise an exception in the try 'block', and if an exception occurs, it is
caught and handled in the 'except' block. This allows you program to handle errors without crashing. It's also possible
to add a specific exception types for more precise error handling.

13) What is a lambda function in Python?

It is a function defined using the 'lambda' keyword. This kind of function is often used for short, simple operations
that can be defined in a single line of code. It's very useful as arguments for higher-order
functions like map(), filter(), sorted()

lambda arguments: expression

a = [1, 2, 3, 4]
b = list(map(lambda x: x**2),a))
c = list(filter(lambda x: x % 2 == 0, a))

dict = {'Luca': 30, 'Gio': 31, 'Marco': 32}
filtered_dict = {k: v for k, v in dict.items() if v > 30}

df = pd.DataFrame({'Name': ['L', 'G', 'M'], 'Age': [30, 31, 31], 'Salary': [100, 200, 300]})
df['Salary] = df['Salary].apply(lambda x: x -50)
filtered_df = df[df['Salary'].apply(lambda x: x > 50)]

14) Explain the purpose of 'with' statement

The with statement in Python is used for context management, particularly in scenarios where resources
need to be acquired and released properly.
It is commonly used with file I/O operations to automatically close files when done

with open('file_name.txt', 'r') as file:
    data = file.read()

15) How can you perform file I/O operations in binary mode?

with open('binary_file.bin' 'rb') as file:
    binary_data = file.read()

16) What is the purpose of 'enumerate' function?

The 'enumerate' function is used to iterate over an iterable while keeping track of the index of each item. It returns
a tuple containing the index and the item of each iteration.

17) How do you create a dictionary in Python?

dict = {'Name' : 'Luca', 'Surname': 'Lombardi', 'Address':'Via Stati Uniti', 'Number' : 34}

18) How can you merge two dictionaries?

dict_b = {'Role' : 'Data Scientist', 'Location' : 'Milan', 'Date' : '2021-12-01'}
dict_c = dict.update(dict_b)

19) What is a generator in Python?

A generator in Python is a special type of iterable that generates values on the fly instead of storing them in memory.
It is defined using a function with the ‘yield’ keyword. Generators are memory-efficient and are often used to process
large datasets or generate an infinite sequence of values.When a generator function is called,
it returns a generator object that can be iterated over using a ‘for’ loop or other iterable operations.

20) How can you reverse a list in Python?

It's possible to reverse a list by using the reverse() method or using slicing.

List = [1, 2, 4, 5]
List.reverse()
reversed_list = List[::-1] in this way you create a reversed list without changing the original one

21) What is the difference between append() and extend() methods for lists?

The append() method is used to add a single element to the end of a list (List.append(6))
The extend() method is used to add elements of an iterable to the end of a list (List.extend(List_2))

22) How do you sort a list?

List = [11, 2, 44, 55, 1]
List.sort()
List_2 = sorted(List)

By default,both methods are sorted in ascending order. To sort in descending order, you can pass the reverse=True argument.

'''
