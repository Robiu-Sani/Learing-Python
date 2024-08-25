# Python Basics

Python is a high-level, interpreted programming language known for its readability and simplicity. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python is widely used for web development, data analysis, artificial intelligence, scientific computing, and automation.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Python Installation](#python-installation)
4. [Python Syntax](#python-syntax)
   - [Hello World](#hello-world)
   - [Variables](#variables)
   - [Data Types](#data-types)
   - [Operators](#operators)
5. [Control Flow](#control-flow)
   - [If-Else Statements](#if-else-statements)
   - [Loops](#loops)
6. [Functions](#functions)
7. [Data Structures](#data-structures)
   - [Lists](#lists)
   - [Tuples](#tuples)
   - [Sets](#sets)
   - [Dictionaries](#dictionaries)
8. [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
9. [Modules and Packages](#modules-and-packages)
10. [File Handling](#file-handling)
11. [Error Handling](#error-handling)
12. [Conclusion](#conclusion)

## Introduction

Python was created by Guido van Rossum and was first released in 1991. It is known for its clear syntax and easy readability, making it an excellent choice for beginners and professionals alike.

## Features

- **Simple and Easy to Learn**: Python has a clean and straightforward syntax that mimics natural language, making it easy to learn.
- **Interpreted Language**: Python code is executed line by line, which makes debugging easier.
- **Cross-Platform**: Python runs on various platforms (Windows, Mac, Linux).
- **Extensive Standard Library**: Python has a vast library of modules and packages that simplify tasks such as file I/O, system calls, and web browsing.
- **Open Source**: Python is free to use and distribute, including for commercial purposes.

## Python Installation

To install Python, download the installer from the [official Python website](https://www.python.org/downloads/) and follow the installation instructions for your operating system.

To check if Python is installed, open a terminal or command prompt and run:

```bash
python --version
```


### Example Code

To print "Hello, World!" in Python, you use the `print()` function. Here’s the code:

```python
print("Hello, World!")
```

## Variables

In Python, a variable is a name that refers to a value. Variables are used to store data that can be referenced and manipulated later in the program.

### Example Code

```python
# Defining variables
name = "Robius"
age = 25
height = 5.9
is_student = True

# Using variables
print(name)        # Output: Robius
print(age)         # Output: 25
print(height)      # Output: 5.9
print(is_student)  # Output: True
```

### Common Data Types

1. **Integers (`int`)**
   - Whole numbers without a fractional part.
   - Example: `5`, `-3`, `100`

   ```python
   number = 10
   print(type(number))  # Output: <class 'int'>

pi = 3.14
print(type(pi))  # Output: <class 'float'>

greeting = "Hello, World!"
print(type(greeting))  # Output: <class 'str'>

is_valid = True
print(type(is_valid))  # Output: <class 'bool'>

fruits = ["apple", "banana", "cherry"]
print(type(fruits))  # Output: <class 'list'>

coordinates = (10, 20)
print(type(coordinates))  # Output: <class 'tuple'>

person = {"name": "Robius", "age": 25}
print(type(person))  # Output: <class 'dict'>

unique_numbers = {1, 2, 3}
print(type(unique_numbers))  # Output: <class 'set'>


```
```
# Converting float to int
num = int(3.14)
print(num)  # Output: 3

# Converting int to string
text = str(25)
print(text)  # Output: '25'
```
