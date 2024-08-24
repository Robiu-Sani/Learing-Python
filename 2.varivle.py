# ----------------- ভ্যারিয়েবল সম্পর্কিত নিয়ম -----------------

# 1. ভ্যারিয়েবল নাম সংখ্যা দিয়ে শুরু করা যাবে না।
# উদাহরণ: 1student = "robius" (ভুল)
# সঠিক উদাহরণ:
student1 = "robius"

# 2. ভ্যারিয়েবল নাম কোনো কীওয়ার্ড হতে পারবে না।
# উদাহরণ: for = "robius" (ভুল)
# সঠিক উদাহরণ:
student_name = "robius"

# 3. ভ্যারিয়েবল নাম অবশ্যই এক শব্দের হতে হবে।
# উদাহরণ: student name = "robius" (ভুল)
# সঠিক উদাহরণ:
student_name = "robius"

# 4. Python case-sensitive:
# student এবং Student আলাদা ভ্যারিয়েবল হিসেবে গণ্য হবে।
student = 'any name'
print(student)  # এটি 'any name' দেখাবে


# ----------------- ডেটা টাইপ -----------------

# 1. স্ট্রিং (String)
name_single_quote = 'robius'
name_double_quote = "robius"
name_triple_quote = """robius"""

# 2. সংখ্যা (Number) বা সাংখ্যিক ডেটা (Numeric)
# ইন্টিজার (Integer) এবং ফ্লোট (Float)
integer_value = 5
float_value = 2.5

# 3. বুলিয়ান (Boolean)
is_valid = True
is_complete = False


# ----------------- অতিরিক্ত মূল্য (Extra Value) -----------------

# প্রিন্ট করার সময় ডাবল কোট দেখানোর জন্য \"
print("He said, \"Hello\"")  # এটি He said, "Hello" দেখাবে

# নতুন লাইনে দেখানোর জন্য \n
print("Hello\nWorld")  # এটি নতুন লাইনে 'World' দেখাবে

# স্ট্রিং সংযোগ করার জন্য +
full_name = "robius" + " " + "sani"
print(full_name)  # এটি 'robius sani' দেখাবে

# ফরম্যাটিং স্ট্রিং (String Formatting)
first_name = "robius"
last_name = "sani"
formatted_name = f"My name is {first_name} {last_name}"
print(formatted_name)  # এটি 'My name is robius sani' দেখাবে


# ----------------- ডেটা টাইপ পরিবর্তন (Type Conversion) -----------------

# 1. স্ট্রিং থেকে ইন্টিজার (String to Integer)
number_str = "5"
number_int = int(number_str)
print(number_int)  # এটি 5 দেখাবে

# 2. স্ট্রিং থেকে ফ্লোট (String to Float)
number_str = "5.5"
number_float = float(number_str)
print(number_float)  # এটি 5.5 দেখাবে

# 3. অন্য ডেটা টাইপ থেকে স্ট্রিং (Any type to String)
number = 5
number_str = str(number)
print(number_str)  # এটি '5' দেখাবে

# 4. অন্য ডেটা টাইপ থেকে বুলিয়ান (Any type to Boolean)
non_empty_str = "robius"
boolean_value = bool(non_empty_str)
print(boolean_value)  # এটি True দেখাবে
