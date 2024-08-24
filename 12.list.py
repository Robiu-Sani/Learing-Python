# lists_in_python.py

# ------------- Basic Information About Lists -------------------

# 1. What is a List?
# ------------------------
# List হল Python এর একটি ডাটা টাইপ যেখানে এক বা একাধিক মান (elements) সংরক্ষণ করা যায়।
# এটি mutable (পরিবর্তনযোগ্য) এবং ordered (ক্রমবদ্ধ)।

# একটি লিস্ট তৈরি করা
my_list = [1, 2, 3, 4, 5]
print("My List:", my_list)  # Output: My List: [1, 2, 3, 4, 5]


# 2. Accessing Elements in a List
# ------------------------
# List এর elements গুলোকে ইন্ডেক্সের মাধ্যমে অ্যাক্সেস করা যায়।
# ইন্ডেক্সিং ০ থেকে শুরু হয়।

# প্রথম ইন্ডেক্সের মান
print("First element:", my_list[0])  # Output: First element: 1

# শেষ ইন্ডেক্সের মান
print("Last element:", my_list[-1])  # Output: Last element: 5


# 3. Modifying a List
# ------------------------
# List এর elements পরিবর্তন করা যায়।

my_list[2] = 10
print("Modified List:", my_list)  # Output: Modified List: [1, 2, 10, 4, 5]


# 4. Adding Elements to a List
# ------------------------
# append(), insert(), extend() ফাংশনগুলো ব্যবহার করে লিস্টে নতুন elements যোগ করা যায়।

# শেষের দিকে একটি নতুন মান যোগ করা
my_list.append(6)
print("List after append:", my_list)  # Output: List after append: [1, 2, 10, 4, 5, 6]

# নির্দিষ্ট ইন্ডেক্সে একটি নতুন মান যোগ করা
my_list.insert(1, 15)
print("List after insert:", my_list)  # Output: List after insert: [1, 15, 2, 10, 4, 5, 6]

# আরেকটি লিস্ট যোগ করা
my_list.extend([7, 8, 9])
print("List after extend:", my_list)  # Output: List after extend: [1, 15, 2, 10, 4, 5, 6, 7, 8, 9]


# 5. Removing Elements from a List
# ------------------------
# pop(), remove(), clear() ফাংশনগুলো ব্যবহার করে লিস্ট থেকে elements সরানো যায়।

# নির্দিষ্ট ইন্ডেক্সের মান সরানো
removed_element = my_list.pop(2)
print("Removed Element:", removed_element)  # Output: Removed Element: 2
print("List after pop:", my_list)  # Output: List after pop: [1, 15, 10, 4, 5, 6, 7, 8, 9]

# নির্দিষ্ট মান সরানো
my_list.remove(10)
print("List after remove:", my_list)  # Output: List after remove: [1, 15, 4, 5, 6, 7, 8, 9]

# লিস্ট সম্পূর্ণ খালি করা
my_list.clear()
print("List after clear:", my_list)  # Output: List after clear: []


# 6. List Slicing
# ------------------------
# লিস্টের নির্দিষ্ট অংশকে স্লাইস করে আনা যায়।

sliced_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Sliced List (2:5):", sliced_list[2:5])  # Output: Sliced List (2:5): [3, 4, 5]

# স্টেপ ব্যবহার করে স্লাইস করা
print("Sliced List (0:9:2):", sliced_list[0:9:2])  # Output: Sliced List (0:9:2): [1, 3, 5, 7, 9]


# 7. List Comprehensions
# ------------------------
# লিস্টের উপরে সহজে এবং দ্রুত কিছু কাজ করার জন্য List Comprehensions ব্যবহার করা হয়।

# ১ থেকে ১০ পর্যন্ত সংখ্যাগুলোর বর্গফল নিয়ে একটি লিস্ট তৈরি করা
squares = [x**2 for x in range(1, 11)]
print("Squares List:", squares)  # Output: Squares List: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# 8. Common List Functions and Methods
# ------------------------

# 8.1 len(): লিস্টের দৈর্ঘ্য বের করা
length = len(sliced_list)
print("Length of sliced_list:", length)  # Output: Length of sliced_list: 9

# 8.2 max(): লিস্টের সর্বোচ্চ মান বের করা
max_value = max(sliced_list)
print("Max value in sliced_list:", max_value)  # Output: Max value in sliced_list: 9

# 8.3 min(): লিস্টের সর্বনিম্ন মান বের করা
min_value = min(sliced_list)
print("Min value in sliced_list:", min_value)  # Output: Min value in sliced_list: 1

# 8.4 sum(): লিস্টের সকল মানের যোগফল বের করা
sum_value = sum(sliced_list)
print("Sum of sliced_list:", sum_value)  # Output: Sum of sliced_list: 45

# 8.5 sort(): লিস্টের মানগুলোকে ক্রমবদ্ধ করা
sliced_list.sort()
print("Sorted List:", sliced_list)  # Output: Sorted List: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 8.6 reverse(): লিস্টের মানগুলোকে উল্টো ক্রমে সাজানো
sliced_list.reverse()
print("Reversed List:", sliced_list)  # Output: Reversed List: [9, 8, 7, 6, 5, 4, 3, 2, 1]


# 9. Advanced List Operations
# ------------------------

# 9.1 Nested Lists
# ------------------------
# লিস্টের ভিতরে লিস্ট রাখা যায়।

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested List:", nested_list)  # Output: Nested List: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Nested List থেকে মান বের করা
print("Element at [1][2]:", nested_list[1][2])  # Output: Element at [1][2]: 6


# 9.2 List of Tuples
# ------------------------
# Tuple দিয়ে লিস্ট তৈরি করা যায়।

list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
print("List of Tuples:", list_of_tuples)  # Output: List of Tuples: [(1, 'a'), (2, 'b'), (3, 'c')]


# 9.3 List with Conditionals
# ------------------------
# লিস্ট কমপ্রিহেনশন এর মধ্যে শর্ত যোগ করা যায়।

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print("Even Squares List:", even_squares)  # Output: Even Squares List: [4, 16, 36, 64, 100]


# 9.4 Flattening a List of Lists
# ------------------------
# একটি লিস্টের ভিতরে আরেকটি লিস্টকে ফ্ল্যাট করে একক লিস্ট তৈরি করা।

flat_list = [item for sublist in nested_list for item in sublist]
print("Flattened List:", flat_list)  # Output: Flattened List: [1, 2, 3, 4, 5, 6, 7, 8, 9]


# 9.5 List Zipping
# ------------------------
# দুটি বা ততোধিক লিস্টকে জিপ করে একত্রিত করা যায়।

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped_list = list(zip(list1, list2))
print("Zipped List:", zipped_list)  # Output: Zipped List: [(1, 'a'), (2, 'b'), (3, 'c')]


# 9.6 Enumerate in Lists
# ------------------------
# লিস্টের প্রতিটি মানের সাথে তার ইন্ডেক্সসহ অ্যাক্সেস করা যায়।

for index, value in enumerate(sliced_list):
    print(f"Index: {index}, Value: {value}")
# Output:
# Index: 0, Value: 9
# Index: 1, Value: 8
# Index: 2, Value: 7
# Index: 3, Value: 6
# Index: 4, Value: 5
# Index: 5, Value: 4
# Index: 6, Value: 3
# Index: 7, Value: 2
# Index: 8, Value: 1


# 10. Copying Lists
# ------------------------
#
