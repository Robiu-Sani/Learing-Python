# dictionaries_in_python.py

# ------------------------ Dictionaries in Python ------------------------

# 1. What is a Dictionary?
# ------------------------
# Dictionary হল একটি ডেটা স্ট্রাকচার যা key-value pair ধারণ করে।
# Key-value pair এর মধ্যে key হয় unique এবং value যেকোনো ধরনের হতে পারে।
# Dictionary তৈরি করা হয় curly braces {} এর মধ্যে key-value pair দিয়ে।

# Example of creating a dictionary:
student = {"name": "Robius", "age": 25, "courses": ["Math", "Science"]}
print(student)  # Output: {'name': 'Robius', 'age': 25, 'courses': ['Math', 'Science']}


# 2. Characteristics of a Dictionary
# ------------------------
# - Unordered: Dictionaries এর মধ্যে elements এর কোন নির্দিষ্ট ক্রম থাকে না (Python 3.7 এর আগে)।
# - Mutable: Dictionary এর মধ্যে elements যোগ, মুছে ফেলা এবং পরিবর্তন করা যায়।
# - Indexed: Dictionary এর মধ্যে elements কে key এর মাধ্যমে অ্যাক্সেস করা হয়।
# - Heterogeneous: Dictionary এর key এবং value যেকোনো ধরনের হতে পারে।

# Example of heterogeneous dictionary:
data = {1: "One", "Two": 2, (3, 4): [3, 4]}
print(data)  # Output: {1: 'One', 'Two': 2, (3, 4): [3, 4]}


# 3. Creating a Dictionary
# ------------------------
# Empty dictionary তৈরি করা:
empty_dict = {}

# Dictionary with data:
person = {"name": "John", "age": 30, "city": "New York"}
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Dictionary using dict() function:
person_via_dict = dict(name="Alice", age=25, city="Paris")
print(person_via_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'Paris'}


# 4. Accessing and Modifying Dictionary Values
# ------------------------
# Accessing values:
print(person["name"])  # Output: John
print(person.get("age"))  # Output: 30

# Modifying values:
person["age"] = 31
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# Adding new key-value pair:
person["email"] = "john@example.com"
print(person)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'email': 'john@example.com'}

# Removing key-value pair using pop():
person.pop("city")
print(person)  # Output: {'name': 'John', 'age': 31, 'email': 'john@example.com'}

# Removing last key-value pair using popitem():
person.popitem()
print(person)  # Output: {'name': 'John', 'age': 31}


# 5. Dictionary Methods
# ------------------------
# Common dictionary methods:

# keys() - Returns a view of all keys:
print(person.keys())  # Output: dict_keys(['name', 'age'])

# values() - Returns a view of all values:
print(person.values())  # Output: dict_values(['John', 31])

# items() - Returns a view of all key-value pairs:
print(person.items())  # Output: dict_items([('name', 'John'), ('age', 31)])

# update() - Updates the dictionary with key-value pairs from another dictionary or iterable:
person.update({"age": 32, "phone": "555-5555"})
print(person)  # Output: {'name': 'John', 'age': 32, 'phone': '555-5555'}

# clear() - Removes all key-value pairs from the dictionary:
person.clear()
print(person)  # Output: {}


# 6. Looping Through a Dictionary
# ------------------------
# Loop through keys:
for key in student:
    print(key)

# Output:
# name
# age
# courses

# Loop through values:
for value in student.values():
    print(value)

# Output:
# Robius
# 25
# ['Math', 'Science']

# Loop through key-value pairs:
for key, value in student.items():
    print(f"{key}: {value}")

# Output:
# name: Robius
# age: 25
# courses: ['Math', 'Science']


# 7. Nested Dictionaries
# ------------------------
# Dictionary এর ভেতরে dictionary রাখতে চাইলে nested dictionary ব্যবহার করা হয়।

students = {
    "student1": {"name": "Alice", "age": 24, "courses": ["Physics", "Chemistry"]},
    "student2": {"name": "Bob", "age": 22, "courses": ["Math", "Biology"]}
}
print(students)  # Output: {'student1': {'name': 'Alice', 'age': 24, 'courses': ['Physics', 'Chemistry']}, 'student2': {'name': 'Bob', 'age': 22, 'courses': ['Math', 'Biology']}}

# Accessing nested dictionary:
print(students["student1"]["name"])  # Output: Alice


# 8. Dictionary Comprehensions
# ------------------------
# Dictionary comprehension হল একটি সংক্ষিপ্ত উপায়ে dictionary তৈরি করার পদ্ধতি, যেটি list comprehension এর মতো কাজ করে।

# Example of dictionary comprehension:
squares = {x: x**2 for x in range(6)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# 9. Dictionary with Default Values
# ------------------------
# defaultdict ব্যবহার করে একটি dictionary তৈরি করা যায় যা একটি default value ধারণ করে।

from collections import defaultdict

# Default factory function for integer:
int_dict = defaultdict(int)
int_dict["a"] += 1
print(int_dict)  # Output: defaultdict(<class 'int'>, {'a': 1})

# Default factory function for list:
list_dict = defaultdict(list)
list_dict["a"].append(1)
print(list_dict)  # Output: defaultdict(<class 'list'>, {'a': [1]})


# 10. Merging Dictionaries
# ------------------------
# Python 3.9 থেকে দুটি dictionary merge করার জন্য | (pipe) অপারেটর ব্যবহার করা যায়।

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Merging using | operator:
merged_dict = dict1 | dict2
print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}


# ------------------------ End of the Python file ------------------------
