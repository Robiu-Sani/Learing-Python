# ternary_operator_example.py

# ---------------- Ternary Operator Example ----------------

# ১. মৌলিক উদাহরণ
age = 18
result = "Eligible to vote" if age >= 18 else "Not eligible to vote"
print("১. মৌলিক উদাহরণ:")
print(result)  # Output: Eligible to vote

# ২. সংখ্যার নির্দিষ্ট পরিসীমা পরীক্ষা
number = 10
result = "Positive" if number > 0 else "Non-positive"
print("\n২. সংখ্যার নির্দিষ্ট পরিসীমা পরীক্ষা:")
print(result)  # Output: Positive

# ৩. ব্যবহারকারীর নামের বৈধতা পরীক্ষা
username = "rob"
valid_username = "Valid username" if len(username) >= 5 else "Invalid username"
print("\n৩. ব্যবহারকারীর নামের বৈধতা পরীক্ষা:")
print(valid_username)  # Output: Invalid username

# ৪. একাধিক শর্ত পরীক্ষা
temperature = 30
weather = "Hot" if temperature > 25 else "Cold"
print("\n৪. একাধিক শর্ত পরীক্ষা:")
print(weather)  # Output: Hot

# ৫. Nested ternary operator ব্যবহার
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print("\n৫. Nested ternary operator ব্যবহার:")
print(grade)  # Output: B

# ৬. ফাংশনে Ternary Operator ব্যবহার
def get_status(is_active):
    return "Active" if is_active else "Inactive"

print("\n৬. ফাংশনে Ternary Operator ব্যবহার:")
print(get_status(True))  # Output: Active
print(get_status(False))  # Output: Inactive

# ৭. লিস্ট কম্প্রিহেনশন ব্যবহার
numbers = [1, 2, 3, 4, 5]
result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print("\n৭. লিস্ট কম্প্রিহেনশন ব্যবহার:")
print(result)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']
