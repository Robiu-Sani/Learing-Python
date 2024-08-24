# loops_example.py

# ---------------- Python Loops ----------------

# 1. For Loop
# ------------------------
# range() একটি বিল্ট-ইন ফাংশন যা একটি নির্দিষ্ট রেঞ্জে সংখ্যার সিকোয়েন্স তৈরি করে। 

# Syntax:
# range(stop)
# range(start, stop)
# range(start, stop, step)
# ------------------------
# For loop ব্যবহৃত হয় একটি সিকোয়েন্সের প্রতিটি আইটেমের উপর পুনরাবৃত্তি করতে।

print("1. For Loop (Basic):")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output: 
# apple
# banana
# cherry

# For loop with range() function
print("\n1. For Loop with range() Function:")
for i in range(3):
    print(i)
# Output:
# 0
# 1
# 2

# For loop with else
print("\n1. For Loop with else:")
for i in range(3):
    print(i)
else:
    print("Loop finished!")
# Output:
# 0
# 1
# 2
# Loop finished!

# Nested For Loop
print("\n1. Nested For Loop:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
# Output:
# i=1, j=1
# i=1, j=2
# i=1, j=3
# i=2, j=1
# i=2, j=2
# i=2, j=3
# i=3, j=1
# i=3, j=2
# i=3, j=3

# 2. While Loop
# ------------------------
# While loop তখন ব্যবহৃত হয় যখন একটি শর্ত পূরণ না হওয়া পর্যন্ত পুনরাবৃত্তি করা হয়।

print("\n2. While Loop (Basic):")
count = 0
while count < 3:
    print("Count:", count)
    count += 1
# Output:
# Count: 0
# Count: 1
# Count: 2

# While loop with else
print("\n2. While Loop with else:")
count = 0
while count < 3:
    print("Count:", count)
    count += 1
else:
    print("Loop finished!")
# Output:
# Count: 0
# Count: 1
# Count: 2
# Loop finished!

# Infinite While Loop (with break)
print("\n2. Infinite While Loop (with break):")
count = 0
while True:
    print("Infinite Loop Count:", count)
    count += 1
    if count == 3:
        break
# Output:
# Infinite Loop Count: 0
# Infinite Loop Count: 1
# Infinite Loop Count: 2

# Nested While Loop
print("\n2. Nested While Loop:")
outer = 1
while outer <= 3:
    inner = 1
    while inner <= 3:
        print(f"outer={outer}, inner={inner}")
        inner += 1
    outer += 1
# Output:
# outer=1, inner=1
# outer=1, inner=2
# outer=1, inner=3
# outer=2, inner=1
# outer=2, inner=2
# outer=2, inner=3
# outer=3, inner=1
# outer=3, inner=2
# outer=3, inner=3

# 3. Loop Control Statements
# ------------------------
# break, continue, and pass are loop control statements used to control the loop execution.

# Break Statement
print("\n3. Break Statement:")
for i in range(5):
    if i == 3:
        break
    print(i)
# Output:
# 0
# 1
# 2

# Continue Statement
print("\n3. Continue Statement:")
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output:
# 0
# 1
# 2
# 4

# Pass Statement
print("\n3. Pass Statement:")
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# Advanced Example: Loop with list comprehension
print("\nAdvanced Example: Loop with List Comprehension:")
squares = [x**2 for x in range(5)]
print(squares)
# Output:
# [0, 1, 4, 9, 16]

# Advanced Example: Loop through dictionary
print("\nAdvanced Example: Loop through Dictionary:")
student_scores = {"Rob": 85, "Tom": 92, "Amy": 78}
for name, score in student_scores.items():
    print(f"{name}: {score}")
# Output:
# Rob: 85
# Tom: 92
# Amy: 78




# break_and_continue_example.py

# ------------- Example using break -----------------

# 1. Break Statement
# ------------------------
# break স্টেটমেন্ট একটি লুপ থেকে বেরিয়ে আসার জন্য ব্যবহার করা হয়।

print("Example of break statement:")
for i in range(1, 11):
    if i == 5:
        break
    print(i)
# Output:
# 1
# 2
# 3
# 4
# (লুপ 5 এ পৌঁছানোর পর ব্রেক হয়ে যায়।)

# ------------- Example using continue -----------------

# 2. Continue Statement
# ------------------------
# continue স্টেটমেন্ট লুপের বাকি অংশ স্কিপ করে পরের ইটারেশনে চলে যায়।

print("\nExample of continue statement:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
# Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10
# (লুপ 5 এ পৌঁছানোর পর ওই ইটারেশন স্কিপ হয়, কিন্তু লুপ বন্ধ হয় না।)



