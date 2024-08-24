# functions_in_python.py

# ------------- Basic Function -------------------

# 1. Basic Function Definition
# ------------------------
# একটি ফাংশন তৈরি করা হয় def কীওয়ার্ড ব্যবহার করে।

def greet():
    """
    এই ফাংশনটি একটি সাধারন অভ্যর্থনা মেসেজ প্রিন্ট করবে।
    """
    print("Hello, Welcome to Python!")

# ফাংশন কল করা
greet()


# 2. Function with Parameters
# ------------------------
# ফাংশনে প্যারামিটার পাস করে তাকে আরও নির্দিষ্ট করা যায়।

def greet_person(name):
    """
    এই ফাংশনটি একটি নির্দিষ্ট ব্যক্তিকে অভ্যর্থনা জানাবে।
    """
    print(f"Hello, {name}! Welcome to Python!")

# ফাংশন কল করা
greet_person("Robius")


# 3. Function with Return Value
# ------------------------
# ফাংশন থেকে একটি মান রিটার্ন করা যায় return কীওয়ার্ড ব্যবহার করে।

def add_numbers(a, b):
    """
    দুটি সংখ্যার যোগফল রিটার্ন করবে।
    """
    return a + b

# ফাংশন কল করা এবং ফলাফল প্রিন্ট করা
result = add_numbers(5, 7)
print("Sum:", result)


# 4. Default Parameters
# ------------------------
# ডিফল্ট প্যারামিটার দিয়ে ফাংশন তৈরি করা যায়। যদি কোন প্যারামিটার পাস না করা হয়, ডিফল্ট মান ব্যবহার হবে।

def greet_person_default(name="Guest"):
    """
    এই ফাংশনটি ডিফল্টভাবে একজন অতিথিকে অভ্যর্থনা জানাবে।
    """
    print(f"Hello, {name}! Welcome to Python!")

# ডিফল্ট প্যারামিটার ব্যবহার করে ফাংশন কল করা
greet_person_default()
greet_person_default("Robius")


# 5. Variable-Length Arguments (*args, **kwargs)
# ------------------------
# ফাংশনে অসীম সংখ্যক প্যারামিটার পাস করা যায় *args এবং **kwargs ব্যবহার করে।

# *args উদাহরণ (tuple হিসেবে প্যারামিটার)
def add_multiple_numbers(*args):
    """
    অসীম সংখ্যক সংখ্যার যোগফল রিটার্ন করবে।
    """
    return sum(args)

# ফাংশন কল করা
print("Sum:", add_multiple_numbers(1, 2, 3, 4, 5))

# **kwargs উদাহরণ (dictionary হিসেবে প্যারামিটার)
def greet_people(**kwargs):
    """
    একাধিক ব্যক্তিকে আলাদা আলাদা অভ্যর্থনা জানাবে।
    """
    for name, greeting in kwargs.items():
        print(f"{greeting}, {name}!")

# ফাংশন কল করা
greet_people(Robius="Hello", Sani="Hi")


# 6. Lambda Function
# ------------------------
# lambda ফাংশন হল একটি ছোট এক্সপ্রেশন যা একটি ফাংশন তৈরি করে।

# সাধারণ ফাংশন
def square(x):
    return x * x

# lambda ফাংশন
square_lambda = lambda x: x * x

print("Square (normal function):", square(5))
print("Square (lambda function):", square_lambda(5))


# 7. Higher-Order Function
# ------------------------
# একটি ফাংশন যা অন্য ফাংশনকে আর্গুমেন্ট হিসেবে গ্রহণ করে।

def apply_function(func, value):
    """
    একটি ফাংশন এবং একটি মান গ্রহণ করে, এবং ফাংশনটি সেই মানের উপর প্রয়োগ করে।
    """
    return func(value)

# lambda ফাংশন ব্যবহার করে
result = apply_function(lambda x: x * 2, 10)
print("Double value:", result)


# 8. Nested Functions
# ------------------------
# একটি ফাংশনের ভিতরে আরেকটি ফাংশন ডিফাইন করা যায়।

def outer_function(text):
    """
    বাইরের ফাংশন যা একটি ভিতরের ফাংশন ডিফাইন করে।
    """
    def inner_function():
        print(text)
    
    # ভিতরের ফাংশন কল করা
    inner_function()

# ফাংশন কল করা
outer_function("Hello from the nested function!")


# 9. Closures
# ------------------------
# একটি নেস্টেড ফাংশন যা বাইরের ফাংশনের ভেরিয়েবলকে ধরে রাখে এবং ব্যবহার করে।

def outer_func(msg):
    """
    ক্লোজার ফাংশন উদাহরণ।
    """
    def inner_func():
        print(msg)
    return inner_func

# ক্লোজার তৈরি করা
closure = outer_func("This is a closure example!")
closure()


# 10. Recursion
# ------------------------
# একটি ফাংশন নিজেই নিজেকে কল করলে তাকে recursion বলে।

def factorial(n):
    """
    একটি সংখ্যার ফ্যাক্টরিয়াল রিটার্ন করবে। (n!)
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# ফাংশন কল করা
print("Factorial of 5:", factorial(5))


# 11. Decorators
# ------------------------
# একটি ফাংশনের কার্যকারিতা পরিবর্তন বা বাড়ানোর জন্য ডেকোরেটর ব্যবহার করা হয়।

def decorator_function(original_function):
    """
    একটি ফাংশন যা ডেকোরেটর হিসাবে কাজ করবে।
    """
    def wrapper_function():
        print("Wrapper executed before", original_function.__name__)
        return original_function()
    return wrapper_function

# ডেকোরেটর ব্যবহার করে ফাংশন সাজানো
@decorator_function
def display():
    print("Display function ran")

# ফাংশন কল করা
display()


# 12. Generator Function
# ------------------------
# generator ফাংশন ব্যবহার করে ইটারেটর তৈরি করা হয়। এটি yield কীওয়ার্ড ব্যবহার করে।

def simple_generator():
    """
    একটি জেনারেটর যা সংখ্যা তৈরি করবে।
    """
    yield 1
    yield 2
    yield 3

# জেনারেটর তৈরি করা
gen = simple_generator()

# জেনারেটর থেকে মান নেয়া
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3


# 13. Function Annotations
# ------------------------
# ফাংশনের প্যারামিটার এবং রিটার্ন টাইপের জন্য টাইপ অ্যানোটেশন যোগ করা যায়।

def add_numbers_annotated(a: int, b: int) -> int:
    """
    দুটি সংখ্যার যোগফল রিটার্ন করবে, টাইপ অ্যানোটেশন সহ।
    """
    return a + b

# ফাংশন কল করা
print("Annotated Sum:", add_numbers_annotated(5, 7))
