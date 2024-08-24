# ---------------- Conditions in Python (শর্ত) ----------------

# ১. if শর্ত: একটি শর্ত সত্য হলে
x = 10
if x > 5:
    print("x is greater than 5")  # এই কোডটি চলবে

# ২. if-else শর্ত: একটি শর্ত সত্য না হলে অন্যটি চলবে
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is less than or equal to 5")  # এই কোডটি চলবে

# ৩. if-elif-else শর্ত: একাধিক শর্ত চেক করা
z = 10
if z < 5:
    print("z is less than 5")
elif z == 10:
    print("z is equal to 10")  # এই কোডটি চলবে
else:
    print("z is greater than 5 and not equal to 10")

# ৪. Nested if: if-এর ভিতরে if
a = 15
if a > 10:
    if a < 20:
        print("a is between 10 and 20")  # এই কোডটি চলবে
    else:
        print("a is greater than or equal to 20")

# ৫. Multiple conditions with and, or: একাধিক শর্ত যুক্ত করা
b = 8
if b > 5 and b < 10:
    print("b is between 5 and 10")  # এই কোডটি চলবে

if b < 5 or b > 10:
    print("b is outside the range 5 to 10")
else:
    print("b is within the range 5 to 10")  # এই কোডটি চলবে

# ---------------- Grade Calculation based on Marks (ফলাফলের ভিত্তিতে গ্রেড নির্ধারণ) ----------------

# গ্রেড নির্ণয়ের জন্য নম্বরের ভিত্তিতে শর্ত প্রয়োগ
marks = 85  # নম্বর (এই মান পরিবর্তন করে বিভিন্ন ফলাফল পরীক্ষা করতে পারেন)

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "A-"
elif marks >= 60:
    grade = "B"
elif marks >= 50:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")


# ---------------- Logical Operators in Python (লজিক্যাল অপারেটর) ----------------

# নম্বরের ভিত্তিতে বিভিন্ন বিষয়ের পাশ বা ফেল নির্ধারণ
math_marks = 75
science_marks = 65
english_marks = 55

# ১. and অপারেটর: সব শর্ত সত্য হলে
# শিক্ষার্থী পাশ করবে যদি তিনটি বিষয়ে ৪০ বা তার বেশি নম্বর পায়
if math_marks >= 40 and science_marks >= 40 and english_marks >= 40:
    print("The student has passed all subjects.")  # এই কোডটি চলবে
else:
    print("The student has failed in one or more subjects.")

# ২. or অপারেটর: এক বা একাধিক শর্ত সত্য হলে
# শিক্ষার্থী অতিরিক্ত সহায়তার প্রয়োজন হবে যদি সে যেকোনো একটি বিষয়েও ৩৫ এর কম পায়
if math_marks < 35 or science_marks < 35 or english_marks < 35:
    print("The student needs additional support.")
else:
    print("The student does not need additional support.")  # এই কোডটি চলবে

# ৩. not অপারেটর: শর্তের বিপরীত চেক করা
# শিক্ষার্থী ফেল করবে না যদি তার সব বিষয়ের নম্বর ৪০ বা তার বেশি হয়
if not (math_marks < 40 or science_marks < 40 or english_marks < 40):
    print("The student has not failed.")  # এই কোডটি চলবে
else:
    print("The student has failed.")

# ---------------- Combined Logical Operators Example (যৌথ লজিক্যাল অপারেটর উদাহরণ) ----------------

# শিক্ষার্থী "Excellent" হবে যদি সে সব বিষয়েই ৭০ বা তার বেশি নম্বর পায়, অন্যথায় "Needs Improvement"
if (math_marks >= 70 and science_marks >= 70 and english_marks >= 70):
    print("The student is Excellent.")  # এই কোডটি চলবে
else:
    print("The student Needs Improvement.")

# শিক্ষার্থী "On Probation" হবে যদি সে যেকোনো দুইটি বিষয়ে ৪০ এর কম পায়, অন্যথায় "Normal"
if (math_marks < 40 and science_marks < 40) or (math_marks < 40 and english_marks < 40) or (science_marks < 40 and english_marks < 40):
    print("The student is On Probation.")
else:
    print("The student is Normal.")  # এই কোডটি চলবে


# ২. উদাহরণ: ব্যবহারকারীর লগইন স্ট্যাটাস যাচাই
is_logged_in = False
has_permission = True

# ব্যবহারকারী যদি লগইন না করে থাকে অথবা অনুমতি না থাকে তবে প্রিন্ট করবে "Access Denied"
if not is_logged_in or not has_permission:
    print("Access Denied.")  # এই কোডটি চলবে