# ---------------- Arithmetic Operators (গাণিতিক অপারেটর) ----------------

a = 10
b = 3

# যোগফল
print(a + b)   # 13
# বিয়োগফল
print(a - b)   # 7
# গুণফল
print(a * b)   # 30
# ভাগফল
print(a / b)   # 3.3333
# মডুলাস: ভাগশেষ
print(a % b)   # 1
# পাওয়ার: শক্তি বা ঘাত
print(a ** b)  # 1000
# ফ্লোর ডিভিশন: পূর্ণসংখ্যায় নামিয়ে আনে
print(a // b)  # 3


# ---------------- Comparison Operators (তুলনামূলক অপারেটর) ----------------

# সমান কি না
print(a == b)  # False
# অসমান কি না
print(a != b)  # True
# বড় কি না
print(a > b)   # True
# ছোট কি না
print(a < b)   # False
# বড় বা সমান কি না
print(a >= b)  # True
# ছোট বা সমান কি না
print(a <= b)  # False


# ---------------- Logical Operators (লজিক্যাল অপারেটর) ----------------

x = True
y = False

# AND অপারেটর: দুইটি শর্তই সত্য হলে
print(x and y)  # False
# OR অপারেটর: দুইটি শর্তের একটি সত্য হলে
print(x or y)   # True
# NOT অপারেটর: শর্তের বিপরীত
print(not x)    # False


# ---------------- Bitwise Operators (বিটওয়াইজ অপারেটর) ----------------

c = 10  # 1010
d = 4   # 0100

# AND অপারেটর: বিট ধরে AND
print(c & d)    # 0000 = 0
# OR অপারেটর: বিট ধরে OR
print(c | d)    # 1110 = 14
# XOR অপারেটর: বিট ধরে XOR
print(c ^ d)    # 1110 = 14
# NOT অপারেটর: বিট ধরে NOT
print(~c)       # -11 (1010 এর বিপরীত)
# বাম শিফট অপারেটর: নির্দিষ্ট সংখ্যক বিট বামে স্থানান্তর
print(c << 2)   # 101000 = 40
# ডান শিফট অপারেটর: নির্দিষ্ট সংখ্যক বিট ডানে স্থানান্তর
print(c >> 2)   # 10 = 2


# ---------------- Assignment Operators (অ্যাসাইনমেন্ট অপারেটর) ----------------

e = 5

# যোগ করে সংরক্ষণ
e += 3  # e = e + 3 = 8
print(e)

# বিয়োগ করে সংরক্ষণ
e -= 2  # e = e - 2 = 6
print(e)

# গুণ করে সংরক্ষণ
e *= 2  # e = e * 2 = 12
print(e)

# ভাগ করে সংরক্ষণ
e /= 3  # e = e / 3 = 4.0
print(e)

# মডুলাস করে সংরক্ষণ
e %= 2  # e = e % 2 = 0.0
print(e)

# ফ্লোর ডিভিশন করে সংরক্ষণ
e = 5
e //= 3  # e = e // 3 = 1
print(e)

# পাওয়ার করে সংরক্ষণ
e **= 3  # e = e ** 3 = 1
print(e)


# ---------------- Membership Operators (সদস্যপদ অপারেটর) ----------------

list_a = [1, 2, 3, 4, 5]

# in অপারেটর: সদস্য কি না
print(3 in list_a)  # True
# not in অপারেটর: সদস্য না কি না
print(6 not in list_a)  # True


# ---------------- Identity Operators (আইডেন্টিটি অপারেটর) ----------------

f = [1, 2, 3]
g = [1, 2, 3]

# is অপারেটর: একই অবজেক্ট কি না
print(f is g)  # False (তারা আলাদা অবজেক্ট)

# is not অপারেটর: আলাদা অবজেক্ট কি না
print(f is not g)  # True


# ---------------- Unary Operators (ইউনারি অপারেটর) ----------------

h = 5

# ঋণাত্মক তৈরি করা
print(-h)  # -5

# ---------------- Other Operators ----------------

# len() = এই ফাংশনটি একটি তালিকার দৈর্ঘ্য প্রদান করে
name = 'robius sani'
print(len(name))  # 11

# নির্দিষ্ট ইন্ডেক্সের মান দেখানো
print(name[4])  # 'u'
print(name[-1])  # 'i'
print(name[0:5])  # 'robiu'

# ---------------- String Functions ----------------

print(name.upper())  # 'ROBIUS SANI'
print(name.lower())  # 'robius sani'
print(name.title())  # 'Robius Sani'
print(name.strip())  # সাদা স্পেস সরানো
print(name.lstrip())  # বামের সাদা স্পেস সরানো
print(name.rstrip())  # ডানের সাদা স্পেস সরানো
print(name.find("us"))  # 'us' এর ইন্ডেক্স 4
print(name.replace("us", "dgdfsdf"))  # 'robidgdfsdf sani'
print("sani" in name)  # True

# ---------------- Variables and Data Types ----------------

# ভ্যারিয়েবল নাম সংখ্যা দিয়ে শুরু করা যাবে না, কীওয়ার্ড হতে পারবে না, একাধিক শব্দ হতে পারবে না
# পাইথন কেস সেনসিটিভ

student = 'any name'
print(student)

# ডাটা টাইপ
# ১. স্ট্রিং => স্ট্রিং একক কোটেশন '', দ্বৈত কোটেশন "", বা তিনটি কোটেশন """ """
# ২. সংখ্যা বা নাম্বারিক = integer => 5 float => 2.5
# ৩. বুলিয়ান (True, False)

# এক্সট্রা ভ্যালু প্রিন্ট = \"
# নতুন লাইন = \n
# সংযোগ = "robius" + "sani"
# ফরম্যাটিং স্ট্রিং = f"কোনো টেক্সট {var name} কোনো টেক্সট {other var name}"

# টাইপ কনভার্শন
print(int("5"))    # 5
print(float("2.5")) # 2.5
print(str(5))      # "5"
print(bool(""))    # False
