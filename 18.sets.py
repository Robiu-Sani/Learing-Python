# sets_in_python.py

# ------------------------ Sets in Python ------------------------

# 1. What is a Set?
# ------------------------
# Set হল একটি ডেটা স্ট্রাকচার যা unordered, mutable, এবং unique elements ধারণ করে। 
# Python-এ, একটি set তৈরি করা হয় curly braces {} ব্যবহার করে অথবা set() ফাংশন দ্বারা।

# Example of creating a set:
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}


# 2. Characteristics of a Set
# ------------------------
# - Unordered: Sets এর মধ্যে elements এর কোন নির্দিষ্ট ক্রম থাকে না।
# - Unique: Set এর প্রতিটি element ইউনিক হয়, অর্থাৎ একই element একাধিকবার থাকতে পারে না।
# - Mutable: Set এর মধ্যে elements যোগ এবং মুছে ফেলা যায়।

# Example of unique elements:
numbers = {1, 2, 2, 3, 4}
print(numbers)  # Output: {1, 2, 3, 4}


# 3. Creating a Set
# ------------------------
# Empty set তৈরি করা:
empty_set = set()  # এটি {} এর মাধ্যমে করা যায় না, কেননা {} একটি খালি ডিকশনারি তৈরি করবে।

# Non-empty set তৈরি করা:
colors = {"red", "green", "blue"}
print(colors)  # Output: {'red', 'green', 'blue'}

# set() constructor ব্যবহার করে:
colors_via_constructor = set(["red", "green", "blue"])
print(colors_via_constructor)  # Output: {'red', 'green', 'blue'}


# 4. Accessing Set Elements
# ------------------------
# Set unordered হওয়ায়, ইন্ডেক্স ব্যবহার করে elements অ্যাক্সেস করা যায় না। 
# তবে loop বা in keyword ব্যবহার করে elements অ্যাক্সেস করা যায়।

for color in colors:
    print(color)

# Output:
# red
# green
# blue


# 5. Adding and Removing Elements in a Set
# ------------------------
# Add a single element:
colors.add("yellow")
print(colors)  # Output: {'red', 'green', 'blue', 'yellow'}

# Add multiple elements:
colors.update(["purple", "orange"])
print(colors)  # Output: {'red', 'green', 'blue', 'yellow', 'purple', 'orange'}

# Remove an element:
colors.remove("yellow")  # যদি element না থাকে, তাহলে KeyError হবে।
print(colors)  # Output: {'red', 'green', 'blue', 'purple', 'orange'}

# Remove an element without raising an error if not found:
colors.discard("yellow")  # KeyError হবে না।
print(colors)  # Output: {'red', 'green', 'blue', 'purple', 'orange'}

# Remove all elements from the set:
colors.clear()
print(colors)  # Output: set()


# 6. Set Operations
# ------------------------
# Set-এ বিভিন্ন ধরনের operations করা যায়, যেমন union, intersection, difference, symmetric difference ইত্যাদি।

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union: দুটি set এর সমস্ত unique elements মিলে একত্রিত করা।
union_set = set_a.union(set_b)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection: দুটি set এর সাধারণ elements গুলো বের করা।
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Output: {4, 5}

# Difference: প্রথম set এর elements থেকে দ্বিতীয় set এর elements গুলো বাদ দেয়া।
difference_set = set_a.difference(set_b)
print(difference_set)  # Output: {1, 2, 3}

# Symmetric Difference: দুটি set এর মাঝে সাধারণ elements বাদ দিয়ে যেগুলো বাকি থাকে।
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}


# 7. Set Membership
# ------------------------
# Set এর মধ্যে কোন element আছে কিনা তা পরীক্ষা করতে in keyword ব্যবহার করা হয়।

# Membership test:
print(3 in set_a)  # Output: True
print(9 in set_b)  # Output: False


# 8. Iterating Through a Set
# ------------------------
# Set এর প্রতিটি element এর উপর loop চালিয়ে তাদের অ্যাক্সেস করা যায়।

for item in set_a:
    print(item)

# Output:
# 1
# 2
# 3
# 4
# 5


# 9. Frozen Sets
# ------------------------
# Frozen set হল একটি immutable version of set, অর্থাৎ এটি তৈরি করার পরে কোন পরিবর্তন করা যায় না।
# এটি hashable হওয়ায় set হিসেবে কাজ করতে পারে এবং dictionary তেও key হিসেবে ব্যবহার করা যায়।

frozen_set_a = frozenset([1, 2, 3, 4, 5])
frozen_set_b = frozenset([4, 5, 6, 7, 8])

# Frozen set এর উপরও set এর মতোই operations চালানো যায়:
print(frozen_set_a.union(frozen_set_b))             # Output: frozenset({1, 2, 3, 4, 5, 6, 7, 8})
print(frozen_set_a.intersection(frozen_set_b))      # Output: frozenset({4, 5})
print(frozen_set_a.difference(frozen_set_b))        # Output: frozenset({1, 2, 3})
print(frozen_set_a.symmetric_difference(frozen_set_b))  # Output: frozenset({1, 2, 3, 6, 7, 8})


# 10. Set Comprehensions
# ------------------------
# Set comprehension হল একটি সংক্ষিপ্ত উপায়ে set তৈরি করার পদ্ধতি, যেটি list comprehension এর মতো কাজ করে।

# Example of set comprehension:
squares = {x**2 for x in range(10)}
print(squares)  # Output: {0, 1, 4, 9, 16, 64, 36, 49, 81, 25}


# ------------------------ End of the Python file ------------------------
