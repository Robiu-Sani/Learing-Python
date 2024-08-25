# find_method_in_python.py

# ------------- Basic Information About find() Method -------------------

# 1. What is find()?
# ------------------------
# `find()` হল একটি বিল্ট-ইন স্ট্রিং মেথড যা একটি সাবস্ট্রিং খুঁজে বের করতে ব্যবহৃত হয়।
# এটি স্ট্রিং এর মধ্যে সাবস্ট্রিং এর প্রথম occurrences এর ইন্ডেক্স রিটার্ন করে।
# যদি সাবস্ট্রিং পাওয়া না যায়, তাহলে এটি -1 রিটার্ন করে।

# 2. Basic Example of find()
# ------------------------
# Example: একটি স্ট্রিং এর মধ্যে একটি সাবস্ট্রিং এর প্রথম অবস্থান খুঁজে বের করা

text = "Hello, welcome to Python programming."
position = text.find("welcome")
print("Position of 'welcome':", position)  # Output: Position of 'welcome': 7


# 3. Using find() when Substring is not Present
# ------------------------
# Example: যদি সাবস্ট্রিং স্ট্রিং এর মধ্যে উপস্থিত না থাকে

position = text.find("Java")
print("Position of 'Java':", position)  # Output: Position of 'Java': -1


# 4. find() with Start and End Parameters
# ------------------------
# `find()` মেথডে start এবং end প্যারামিটার ব্যবহার করে সাবস্ট্রিং এর সন্ধান নির্দিষ্ট অংশে সীমাবদ্ধ করা যায়।

text = "Python is fun. Python is powerful."
position = text.find("Python", 10)
print("Position of 'Python' after index 10:", position)  # Output: Position of 'Python' after index 10: 16

# Specifying both start and end
position = text.find("Python", 10, 30)
print("Position of 'Python' between index 10 and 30:", position)  # Output: Position of 'Python' between index 10 and 30: 16


# 5. Finding Multiple Occurrences of a Substring
# ------------------------
# Example: একটি সাবস্ট্রিং এর একাধিক occurrences খুঁজে বের করা

text = "abracadabra"
positions = []
index = text.find("a")

while index != -1:
    positions.append(index)
    index = text.find("a", index + 1)

print("All positions of 'a':", positions)  # Output: All positions of 'a': [0, 3, 5, 7, 10]


# 6. Using find() in Case-Insensitive Search
# ------------------------
# Example: বড় হাতের অক্ষর এবং ছোট হাতের অক্ষর এর পার্থক্য না করে সাবস্ট্রিং খুঁজে বের করা

text = "Hello, Welcome to PYTHON programming."
position = text.lower().find("python")
print("Position of 'python' (case-insensitive):", position)  # Output: Position of 'python' (case-insensitive): 18


# 7. Using find() with User Input
# ------------------------
# Example: ব্যবহারকারীর ইনপুট থেকে সাবস্ট্রিং খুঁজে বের করা

text = "The quick brown fox jumps over the lazy dog."
search_term = input("Enter the word to find: ").strip()
position = text.find(search_term)

if position != -1:
    print(f"'{search_term}' found at position: {position}")
else:
    print(f"'{search_term}' not found in the text.")

# Output example:
# Enter the word to find: fox
# 'fox' found at position: 16


# 8. Advanced Example: Finding the First Non-Repeating Character
# ------------------------
# Example: একটি স্ট্রিং এর প্রথম non-repeating চরিত্র খুঁজে বের করা

def find_first_non_repeating_char(text):
    for i, char in enumerate(text):
        if text.find(char) == text.rfind(char):
            return char, i
    return None, -1

text = "swiss"
char, position = find_first_non_repeating_char(text)

if position != -1:
    print(f"First non-repeating character: '{char}' at position {position}")
else:
    print("No non-repeating character found.")

# Output: First non-repeating character: 'w' at position 1


# ------------- End of the Python file -------------------
