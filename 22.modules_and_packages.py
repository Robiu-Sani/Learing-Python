# modules_and_packages.py

# ------------- Modules and Packages in Python -------------------

# 1. What is a Module?
# -----------------------
# Module হলো একটি ফাইল যেটিতে Python কোড (functions, classes, variables ইত্যাদি) লেখা থাকে। 
# Python-এ প্রতিটি `.py` ফাইলই একটি Module হিসেবে বিবেচিত হয়।
# Module ব্যবহার করে কোডকে সংগঠিত এবং পুনঃব্যবহারযোগ্য করা যায়।

# Example: mymodule.py (a simple module)
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

# `mymodule.py` ফাইলটিকে একটি Module হিসেবে ব্যবহার করা যেতে পারে।

# Usage:
import mymodule

print(mymodule.greet("Robius"))  # Output: Hello, Robius!
print(mymodule.add(2, 3))       # Output: 5

# 2. Importing Modules
# -----------------------
# Python-এ Module import করার জন্য `import` statement ব্যবহার করা হয়।
# পুরো Module import করা, specific function বা class import করা, বা alias দিয়ে import করা যায়।

# Import the entire module:
import mymodule

# Import specific function from the module:
from mymodule import greet

# Import with an alias:
import mymodule as mm

# 3. Built-in Modules
# -----------------------
# Python-এ অনেকগুলো built-in module আছে যেগুলো বিভিন্ন কাজের জন্য ব্যবহার করা যায়।
# যেমন: `math`, `os`, `random`, `sys`, ইত্যাদি।

import math
print(math.sqrt(16))  # Output: 4.0

import random
print(random.randint(1, 10))  # Output: Random number between 1 and 10

# 4. Custom Modules
# -----------------------
# আপনি নিজের মতো করে custom modules তৈরি করতে পারেন।
# নিচে `mymath.py` নামে একটি custom module-এর উদাহরণ দেয়া হলো।

# mymath.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

# Usage:
import mymath

print(mymath.add(10, 5))       # Output: 15
print(mymath.divide(10, 0))    # Output: Cannot divide by zero!

# 5. What is a Package?
# -----------------------
# Package হলো একটি directory যেটিতে এক বা একাধিক Python মডিউল থাকতে পারে। 
# সাধারণত একটি package একটি `__init__.py` ফাইলের মাধ্যমে চিহ্নিত করা হয়।

# Example: A package structure
# mypackage/
# ├── __init__.py
# ├── module1.py
# └── module2.py

# `__init__.py` ফাইলটি package হিসেবে directory-কে চিহ্নিত করে। 

# Usage:
# from mypackage import module1
# from mypackage.module2 import function_name

# 6. Importing from a Package
# -----------------------
# আপনি package থেকে নির্দিষ্ট module বা function import করতে পারেন।

# Example:
# from mypackage import module1
# from mypackage.module2 import function_name

# 7. __init__.py File
# -----------------------
# `__init__.py` ফাইলটি একটি package হিসেবে directory-কে চিহ্নিত করে। 
# Python 3.3 থেকে এটি opsional হয়ে গেছে, কিন্তু convention হিসেবে অনেকেই এটি ব্যবহার করে থাকে।
# এই ফাইলটি মডিউলগুলোকে package-এর অংশ হিসেবে ব্যবহৃত করার সুযোগ দেয়।

# Example of __init__.py:
# __init__.py
from .module1 import some_function
from .module2 import another_function

# 8. Relative Imports
# -----------------------
# Package এর ভিতরে এক module থেকে অন্য module import করতে গেলে relative import ব্যবহার করা হয়।

# Example:
# from .module1 import some_function

# 9. Creating and Using Packages
# -----------------------
# একটি package তৈরি করতে হলে, আপনার directory structure এ .py ফাইলগুলো যোগ করে package-এর মতো তৈরি করতে হবে।

# Example:
# mypackage/
# ├── __init__.py
# ├── math_operations/
# │   ├── __init__.py
# │   ├── add.py
# │   └── subtract.py
# └── string_operations/
#     ├── __init__.py
#     ├── concat.py
#     └── split.py

# Package usage:
# from mypackage.math_operations.add import add_numbers
# from mypackage.string_operations.concat import concat_strings

# 10. Installing Packages
# -----------------------
# Python Package Index (PyPI) থেকে packages ইনস্টল করার জন্য `pip` ব্যবহার করা হয়।

# Example:
# pip install numpy

# Usage:
import numpy as np
arr = np.array([1, 2, 3])
print(arr)  # Output: [1 2 3]

# 11. Namespace Packages
# -----------------------
# Namespace package হলো এমন একটি package যেটি `__init__.py` ফাইল ছাড়া বিভিন্ন directories-এ ছড়িয়ে থাকতে পারে।

# Example:
# ├── mynamespace/
# │   └── foo/
# │       ├── __init__.py
# │       └── foo1.py
# └── anothernamespace/
#     └── foo/
#         ├── __init__.py
#         └── foo2.py

# Usage:
# from mynamespace.foo import foo1
# from anothernamespace.foo import foo2

# 12. Advanced: Importing from a Subdirectory
# -----------------------
# আপনি subdirectory থেকে মডিউল import করতে পারেন যদি সেই directory আপনার sys.path-এ থাকে অথবা তা package-এর অংশ হয়।

# Example structure:
# project/
# ├── main.py
# └── subdir/
#     ├── __init__.py
#     └── submodule.py

# main.py এর ভিতর থেকে submodule import করতে পারেন:
# from subdir import submodule

# 13. `__all__` in Modules and Packages
# -----------------------
# `__all__` variable ব্যবহার করে নির্ধারণ করতে পারেন কোন কোন মডিউল বা ফাংশন বাইরে থেকে import করা যাবে।

# Example:
# __init__.py
# __all__ = ["module1", "module2"]

# Importing from a package:
# from mypackage import *

# 14. Dynamic Import
# -----------------------
# Python-এ আপনি dynamic ভাবে import করতে পারেন `importlib` module ব্যবহার করে।

import importlib

module_name = "math"
math_module = importlib.import_module(module_name)
print(math_module.sqrt(16))  # Output: 4.0

# Conclusion:
# -----------------------
# Modules এবং Packages ব্যবহারের মাধ্যমে আপনি আপনার কোডকে সংগঠিত, পুনঃব্যবহারযোগ্য, এবং সহজে পরিচালনা করতে পারেন।
# এটি একটি কার্যকরী পদ্ধতি বড় প্রজেক্টে যেখানে অনেক কোড থাকে।
