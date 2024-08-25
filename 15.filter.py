# filter_function_in_python.py

# ------------- Basic Information About filter() Function -------------------

# 1. What is filter()?
# ------------------------
# `filter()` হল একটি বিল্ট-ইন ফাংশন যা একটি নির্দিষ্ট ফাংশনকে একটি iterable এর প্রতিটি আইটেমের উপর প্রয়োগ করে
# এবং শুধুমাত্র সেই আইটেমগুলোকে রিটার্ন করে যেগুলোর জন্য ফাংশনটি True রিটার্ন করে।

# 2. Basic Example of filter()
# ------------------------
# Example: একটি লিস্ট থেকে পজিটিভ সংখ্যাগুলো বের করা

def is_positive(x):
    return x > 0

numbers = [-2, -1, 0, 1, 2]
result = filter(is_positive, numbers)
print("Positive Numbers:", list(result))  # Output: Positive Numbers: [1, 2]


# 3. Using filter() with a Lambda Function
# ------------------------
# Lambda ফাংশন ব্যবহার করে filter() কে আরও সংক্ষিপ্ত করা যায়।

numbers = [-2, -1, 0, 1, 2]
result = filter(lambda x: x > 0, numbers)
print("Positive Numbers with Lambda:", list(result))  # Output: Positive Numbers with Lambda: [1, 2]


# 4. Filtering with Strings
# ------------------------
# Example: একটি লিস্ট থেকে নির্দিষ্ট স্ট্রিং বের করা

words = ["hello", "world", "python", "filter", "function"]
result = filter(lambda word: len(word) > 5, words)
print("Words longer than 5 characters:", list(result))  # Output: Words longer than 5 characters: ['python', 'filter', 'function']


# 5. Filtering with Tuples
# ------------------------
# filter() টুপল এর উপরেও কাজ করতে পারে।
# Example: একটি টুপল থেকে পজিটিভ সংখ্যাগুলো বের করা

numbers_tuple = (-5, 3, -1, 101, 0)
result = filter(lambda x: x > 0, numbers_tuple)
print("Positive Tuple Values:", tuple(result))  # Output: Positive Tuple Values: (3, 101)


# 6. Filtering with Lists of Dictionaries
# ------------------------
# Example: একটি লিস্টের মধ্যে থাকা ডিকশনারি থেকে নির্দিষ্ট কন্ডিশনের আইটেমগুলো বের করা

people = [
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 30}
]

result = filter(lambda person: person["age"] > 25, people)
print("People older than 25:", list(result))
# Output: People older than 25: [{'name': 'Alice', 'age': 28}, {'name': 'Charlie', 'age': 30}]


# 7. Combining map() and filter()
# ------------------------
# map() এবং filter() একসাথে ব্যবহার করা যায়।
# Example: একটি লিস্ট থেকে পজিটিভ সংখ্যার স্কোয়ার বের করা

numbers = [-2, -1, 0, 1, 2]
result = map(lambda x: x ** 2, filter(lambda x: x > 0, numbers))
print("Squares of Positive Numbers:", list(result))  # Output: Squares of Positive Numbers: [1, 4]


# 8. Using filter() with None
# ------------------------
# যদি filter() এর ফাংশন আর্গুমেন্ট None থাকে, তাহলে iterable এর ফালসি মান (যেমন: 0, '', None) বাদ দেয়া হয়।

mixed_list = [0, 1, False, True, '', 'Hello', None, 'Python']
result = filter(None, mixed_list)
print("Filtered Truthy Values:", list(result))  # Output: Filtered Truthy Values: [1, True, 'Hello', 'Python']


# 9. Advanced Example: Filtering Even Numbers from Multiple Iterables
# ------------------------
# Example: একাধিক iterable থেকে শুধুমাত্র ইভেন সংখ্যা বের করা

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 11, 12, 13, 14]
result = filter(lambda x: x % 2 == 0, numbers1 + numbers2)
print("Even Numbers from Multiple Iterables:", list(result))
# Output: Even Numbers from Multiple Iterables: [2, 4, 10, 12, 14]


# 10. Filtering Objects Based on Attributes
# ------------------------
# Example: একটি ক্লাসের অবজেক্টগুলোর নির্দিষ্ট attribute এর উপর ভিত্তি করে ফিল্টার করা

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

products = [
    Product("Laptop", 1200),
    Product("Mouse", 20),
    Product("Keyboard", 100),
    Product("Monitor", 300)
]

result = filter(lambda product: product.price > 100, products)
filtered_products = list(result)
print("Products with Price Greater than 100:")
for product in filtered_products:
    print(f"{product.name}: ${product.price}")
# Output:
# Products with Price Greater than 100:
# Laptop: $1200
# Monitor: $300


# ------------- End of the Python file -------------------
