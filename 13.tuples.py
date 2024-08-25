# tuples_in_python.py

# ------------- Basic Information About Tuples -------------------

# 1. What is a Tuple?
# ------------------------
# Tuple হল Python এর একটি ডাটা টাইপ যা একাধিক মান সংরক্ষণ করতে পারে।
# এটি immutable (পরিবর্তনযোগ্য নয়) এবং ordered (ক্রমবদ্ধ)।

# একটি tuple তৈরি করা
my_tuple = (1, 2, 3, 4, 5)
print("My Tuple:", my_tuple)  # Output: My Tuple: (1, 2, 3, 4, 5)


# 2. Accessing Elements in a Tuple
# ------------------------
# Tuple এর elements গুলোকে ইন্ডেক্সের মাধ্যমে অ্যাক্সেস করা যায়।
# ইন্ডেক্সিং ০ থেকে শুরু হয়।

# প্রথম ইন্ডেক্সের মান
print("First element:", my_tuple[0])  # Output: First element: 1

# শেষ ইন্ডেক্সের মান
print("Last element:", my_tuple[-1])  # Output: Last element: 5


# 3. Tuple Immutability
# ------------------------
# Tuple এর elements পরিবর্তন করা যায় না।

# Example:
# my_tuple[1] = 10  # এটি একটি error তৈরি করবে: TypeError: 'tuple' object does not support item assignment


# 4. Creating a Tuple with One Element
# ------------------------
# একটিমাত্র মান দিয়ে Tuple তৈরি করতে হলে, মানের পরে একটি কমা (,) দিতে হবে।

single_element_tuple = (42,)
print("Single Element Tuple:", single_element_tuple)  # Output: Single Element Tuple: (42,)


# 5. Tuple Packing and Unpacking
# ------------------------
# Tuple Packing: একাধিক মানের সমষ্টিকে একটি Tuple এ প্যাক করা।
# Tuple Unpacking: একটি Tuple এর মানগুলোকে পৃথক ভেরিয়েবলে আনপ্যাক করা।

# Packing
packed_tuple = 10, 20, 30
print("Packed Tuple:", packed_tuple)  # Output: Packed Tuple: (10, 20, 30)

# Unpacking
a, b, c = packed_tuple
print("Unpacked Values:", a, b, c)  # Output: Unpacked Values: 10 20 30


# 6. Tuple with Different Data Types
# ------------------------
# Tuple বিভিন্ন ধরনের ডাটা সংরক্ষণ করতে পারে।

mixed_tuple = (1, "Hello", 3.14, True)
print("Mixed Tuple:", mixed_tuple)  # Output: Mixed Tuple: (1, 'Hello', 3.14, True)


# 7. Nested Tuples
# ------------------------
# Tuple এর ভিতরে আরেকটি Tuple রাখা যায়।

nested_tuple = (1, (2, 3), (4, 5, 6))
print("Nested Tuple:", nested_tuple)  # Output: Nested Tuple: (1, (2, 3), (4, 5, 6))

# Nested Tuple থেকে মান বের করা
print("Element at [1][1]:", nested_tuple[1][1])  # Output: Element at [1][1]: 3


# 8. Tuple Slicing
# ------------------------
# Tuple এর নির্দিষ্ট অংশকে স্লাইস করে আনা যায়।

sliced_tuple = my_tuple[1:4]
print("Sliced Tuple (1:4):", sliced_tuple)  # Output: Sliced Tuple (1:4): (2, 3, 4)

# স্টেপ ব্যবহার করে স্লাইস করা
print("Sliced Tuple (0:5:2):", my_tuple[0:5:2])  # Output: Sliced Tuple (0:5:2): (1, 3, 5)


# 9. Common Tuple Functions and Methods
# ------------------------

# 9.1 len(): Tuple এর দৈর্ঘ্য বের করা
length = len(my_tuple)
print("Length of my_tuple:", length)  # Output: Length of my_tuple: 5

# 9.2 max(): Tuple এর সর্বোচ্চ মান বের করা (সমস্ত মান একই ধরনের হতে হবে)
max_value = max(my_tuple)
print("Max value in my_tuple:", max_value)  # Output: Max value in my_tuple: 5

# 9.3 min(): Tuple এর সর্বনিম্ন মান বের করা (সমস্ত মান একই ধরনের হতে হবে)
min_value = min(my_tuple)
print("Min value in my_tuple:", min_value)  # Output: Min value in my_tuple: 1

# 9.4 sum(): Tuple এর সকল মানের যোগফল বের করা (সমস্ত মান সংখ্যা হতে হবে)
sum_value = sum(my_tuple)
print("Sum of my_tuple:", sum_value)  # Output: Sum of my_tuple: 15

# 9.5 count(): Tuple এর মধ্যে নির্দিষ্ট মান কতবার আছে তা বের করা
count_value = my_tuple.count(3)
print("Count of 3 in my_tuple:", count_value)  # Output: Count of 3 in my_tuple: 1

# 9.6 index(): Tuple এর মধ্যে নির্দিষ্ট মানের ইন্ডেক্স বের করা
index_value = my_tuple.index(4)
print("Index of 4 in my_tuple:", index_value)  # Output: Index of 4 in my_tuple: 3


# 10. Tuple Membership
# ------------------------
# Tuple এর মধ্যে কোনো মান আছে কিনা তা চেক করা যায়।

print("Is 4 in my_tuple?", 4 in my_tuple)  # Output: Is 4 in my_tuple? True
print("Is 10 in my_tuple?", 10 in my_tuple)  # Output: Is 10 in my_tuple? False


# 11. Looping Through Tuples
# ------------------------
# Tuple এর প্রতিটি মানের উপর লুপ চালানো যায়।

for item in my_tuple:
    print("Item:", item)
# Output:
# Item: 1
# Item: 2
# Item: 3
# Item: 4
# Item: 5


# 12. Tuple Concatenation
# ------------------------
# দুটি বা ততোধিক Tuple কে একত্রিত করা যায়।

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tuple)  # Output: Concatenated Tuple: (1, 2, 3, 4, 5, 6)


# 13. Tuple Multiplication
# ------------------------
# একটি Tuple কে নির্দিষ্ট বার রিপিট করা যায়।

repeated_tuple = tuple1 * 3
print("Repeated Tuple:", repeated_tuple)  # Output: Repeated Tuple: (1, 2, 3, 1, 2, 3, 1, 2, 3)


# 14. Advanced Tuple Operations
# ------------------------

# 14.1 Tuple of Tuples
# ------------------------
# Tuple এর মধ্যে আরেকটি Tuple রাখা যায়।

tuple_of_tuples = ((1, 2), (3, 4), (5, 6))
print("Tuple of Tuples:", tuple_of_tuples)  # Output: Tuple of Tuples: ((1, 2), (3, 4), (5, 6))

# Tuple of Tuples থেকে মান বের করা
print("Element at [1][0]:", tuple_of_tuples[1][0])  # Output: Element at [1][0]: 3


# 14.2 Tuple Comprehensions (Using Generator Expression)
# ------------------------
# Tuple এর ভিতরে দ্রুত কিছু কাজ করার জন্য Generator Expression ব্যবহার করা হয়।
# Note: This creates a generator, not a tuple.

# Example: ১ থেকে ১০ পর্যন্ত সংখ্যাগুলোর বর্গফল নিয়ে একটি generator তৈরি করা
squares = (x**2 for x in range(1, 11))
print("Tuple Comprehension (Generator):", tuple(squares))  # Output: Tuple Comprehension (Generator): (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)


# 14.3 Zipping Tuples
# ------------------------
# দুটি বা ততোধিক Tuple কে জিপ করে একত্রিত করা যায়।

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped_tuple = tuple(zip(tuple1, tuple2))
print("Zipped Tuple:", zipped_tuple)  # Output: Zipped Tuple: ((1, 'a'), (2, 'b'), (3, 'c'))


# 14.4 Enumerate in Tuples
# ------------------------
# Tuple এর প্রতিটি মানের সাথে তার ইন্ডেক্সসহ অ্যাক্সেস করা যায়।

for index, value in enumerate(my_tuple):
    print(f"Index: {index}, Value: {value}")
# Output:
# Index: 0, Value: 1
# Index: 1, Value: 2
# Index: 2, Value: 3
# Index: 3, Value: 4
# Index: 4, Value: 5


# 15. Copying Tuples
# ------------------------
# Tuple কপি করার কিছু পদ্ধতি রয়েছে, কিন্তু Tuple immutable হওয়ায় সরাসরি কপি করা সহজ।

# সরাসরি কপি
copy_tuple = my_tuple
print("Copy of my_tuple:", copy_tuple)  # Output: Copy of my_tuple: (1, 2, 3, 4, 5)

# Tuple constructor ব্যবহার করে কপি করা
copy_tuple2 = tuple(my_tuple)
print("Copy of my_tuple using tuple():", copy_tuple2)  # Output: Copy of my_tuple using tuple(): (1, 2, 3, 4, 5)


# ------------- End of the Python file -------------------
