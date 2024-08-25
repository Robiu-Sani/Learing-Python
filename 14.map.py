# map_function_in_python.py

# ------------- Basic Information About map() Function -------------------

# 1. What is map()?
# ------------------------
# `map()` হল একটি বিল্ট-ইন ফাংশন যা একটি নির্দিষ্ট ফাংশনকে একটি বা একাধিক iterable এর প্রতিটি আইটেমের উপর প্রয়োগ করে
# এবং একটি map অবজেক্ট (iterator) রিটার্ন করে।

# 2. Basic Example of map()
# ------------------------
# Example: একটি লিস্টের প্রতিটি সংখ্যা দ্বিগুণ করা

def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
result = map(double, numbers)
print("Doubled Numbers:", list(result))  # Output: Doubled Numbers: [2, 4, 6, 8, 10]


# 3. Using map() with a Lambda Function
# ------------------------
# Lambda ফাংশন ব্যবহার করে map() কে আরও সংক্ষিপ্ত করা যায়।

numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers)
print("Doubled Numbers with Lambda:", list(result))  # Output: Doubled Numbers with Lambda: [2, 4, 6, 8, 10]


# 4. Mapping Multiple Iterables
# ------------------------
# map() ফাংশনকে একাধিক iterable এর উপর প্রয়োগ করা যায়।
# Example: দুটি লিস্টের corresponding মানগুলো যোগ করা

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print("Sum of Corresponding Numbers:", list(result))  # Output: Sum of Corresponding Numbers: [5, 7, 9]


# 5. Converting map Object to List
# ------------------------
# map() একটি map অবজেক্ট (iterator) রিটার্ন করে, যেটিকে আমরা list() ফাংশন দিয়ে লিস্টে রূপান্তর করতে পারি।

numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers)
result_list = list(result)
print("Result as List:", result_list)  # Output: Result as List: [2, 4, 6, 8, 10]


# 6. Using map() with Built-in Functions
# ------------------------
# map() ফাংশনের সাথে Python এর বিল্ট-ইন ফাংশন ব্যবহার করা যায়।
# Example: প্রতিটি সংখ্যার absolute মান বের করা

numbers = [-1, -2, 3, -4, 5]
result = map(abs, numbers)
print("Absolute Values:", list(result))  # Output: Absolute Values: [1, 2, 3, 4, 5]


# 7. Mapping with Strings
# ------------------------
# Example: একটি লিস্টের প্রতিটি স্ট্রিংকে uppercase এ রূপান্তর করা

words = ["hello", "world", "python"]
result = map(str.upper, words)
print("Uppercase Words:", list(result))  # Output: Uppercase Words: ['HELLO', 'WORLD', 'PYTHON']


# 8. Mapping with Tuples
# ------------------------
# map() টুপল এর উপরেও কাজ করতে পারে।
# Example: একটি টুপলের প্রতিটি মানের উপর ফাংশন প্রয়োগ করা

numbers_tuple = (1, 2, 3, 4, 5)
result = map(lambda x: x * 3, numbers_tuple)
print("Tripled Tuple Values:", tuple(result))  # Output: Tripled Tuple Values: (3, 6, 9, 12, 15)


# 9. Advanced Example: Mapping with Multiple Functions
# ------------------------
# map() ফাংশনকে একাধিক ফাংশনের সাথে ব্যবহার করে বিভিন্ন ফলাফল বের করা যায়।
# Example: একটি লিস্টের প্রতিটি সংখ্যার স্কোয়ার ও কিউব বের করা

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

functions = [square, cube]
numbers = [2, 3, 4]

for i in numbers:
    result = list(map(lambda f: f(i), functions))
    print(f"Number {i}: Square = {result[0]}, Cube = {result[1]}")
# Output:
# Number 2: Square = 4, Cube = 8
# Number 3: Square = 9, Cube = 27
# Number 4: Square = 16, Cube = 64


# 10. Filtering with map() (combined with filter)
# ------------------------
# map() এবং filter() একসাথে ব্যবহার করে ডাটা ফিল্টারিং ও প্রসেস করা যায়।
# Example: একটি লিস্ট থেকে শুধু পজিটিভ স্কোয়ার বের করা

numbers = [-2, -1, 0, 1, 2]
result = map(lambda x: x ** 2, filter(lambda y: y > 0, numbers))
print("Positive Squares:", list(result))  # Output: Positive Squares: [1, 4]


# ------------- End of the Python file -------------------
