# comprehensions_in_python.py

# ------------- Comprehensions in Python: Basic to Advanced -------------------

# 1. What is Comprehension?
# ------------------------
# Comprehension হল একটি সংক্ষিপ্ত উপায় যা দিয়ে আমরা লুপ ব্যবহার করে একাধিক মান 
# নিয়ে একটি নতুন লিস্ট, সেট, বা ডিকশনারি তৈরি করতে পারি।

# 2. List Comprehension
# ------------------------
# Basic Example:
# একটি লিস্টের সব মানকে দ্বিগুণ করা

numbers = [1, 2, 3, 4, 5]
doubled_numbers = [n * 2 for n in numbers]
print("Doubled Numbers:", doubled_numbers)  # Output: [2, 4, 6, 8, 10]

# List Comprehension with Condition:
# শুধুমাত্র জোড় সংখ্যাগুলি দ্বিগুণ করা

even_doubled = [n * 2 for n in numbers if n % 2 == 0]
print("Even Doubled Numbers:", even_doubled)  # Output: [4, 8]

# Nested List Comprehension:
# একটি 2D লিস্টের প্রতিটি মানকে দ্বিগুণ করা

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
doubled_matrix = [[n * 2 for n in row] for row in matrix]
print("Doubled Matrix:", doubled_matrix)  # Output: [[2, 4, 6], [8, 10, 12], [14, 16, 18]]


# 3. Dictionary Comprehension
# ------------------------
# Basic Example:
# একটি ডিকশনারির সব ভ্যালুকে দ্বিগুণ করা

ages = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
doubled_ages = {name: age * 2 for name, age in ages.items()}
print("Doubled Ages:", doubled_ages)  # Output: {'Alice': 50, 'Bob': 60, 'Charlie': 70}

# Dictionary Comprehension with Condition:
# শুধুমাত্র যাদের বয়স ৩০ এর উপরে তাদের নাম ও বয়স রাখুন

filtered_ages = {name: age for name, age in ages.items() if age > 30}
print("Filtered Ages:", filtered_ages)  # Output: {'Charlie': 35}

# Nested Dictionary Comprehension:
# একটি nested dictionary তৈরি করা

nested_dict = {i: {j: i * j for j in range(1, 4)} for i in range(1, 4)}
print("Nested Dictionary:", nested_dict)
# Output: 
# {
#   1: {1: 1, 2: 2, 3: 3},
#   2: {1: 2, 2: 4, 3: 6},
#   3: {1: 3, 2: 6, 3: 9}
# }


# 4. Set Comprehension
# ------------------------
# Basic Example:
# একটি লিস্টের unique মানগুলি একটি সেটে রাখা

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = {n for n in numbers}
print("Unique Numbers:", unique_numbers)  # Output: {1, 2, 3, 4, 5}

# Set Comprehension with Condition:
# শুধুমাত্র জোড় সংখ্যাগুলি একটি সেটে রাখা

even_numbers = {n for n in numbers if n % 2 == 0}
print("Even Numbers:", even_numbers)  # Output: {2, 4}

# Advanced Set Comprehension:
# একটি লিস্টের অনন্য বর্গমূলের মানগুলি বের করা

import math
squares = {math.sqrt(n) for n in range(1, 10)}
print("Unique Square Roots:", squares)  # Output: {1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0}


# 5. Advanced List Comprehension Techniques
# ------------------------
# Flattening a 2D List:
# একটি 2D লিস্টকে একটি 1D লিস্টে রূপান্তর করা

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [n for row in matrix for n in row]
print("Flattened List:", flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List Comprehension with Multiple Conditions:
# একটি লিস্টের সব positive এবং জোড় সংখ্যাগুলি রাখুন

numbers = [-5, -4, -3, 0, 2, 4, 6]
filtered_numbers = [n for n in numbers if n > 0 and n % 2 == 0]
print("Filtered Numbers:", filtered_numbers)  # Output: [2, 4, 6]


# 6. Using Functions in Comprehension
# ------------------------
# Example: একটি ফাংশন ব্যবহার করে list comprehension এর মধ্যে বর্গমূল বের করা

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = [square(n) for n in numbers]
print("Squared Numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]


# ------------- End of the Python file -------------------
