# __init__: নতুন object তৈরি করার সময় initial state সেট করে।
# __str__: object কে readable string হিসেবে প্রিন্ট করে।
# __repr__: object-এর আনুষ্ঠানিক string রিপ্রেজেন্টেশন প্রদান করে।
# __len__: object-এর দৈর্ঘ্য প্রদান করে।
# __add__: দুটি object-এর যোগফল নির্ধারণ করে।
# __eq__: দুটি object-এর সমতা নির্ধারণ করে।
# __getitem__: object থেকে একটি item আনে।
# __setitem__: object এ একটি item সেট করে।
# __delitem__: object থেকে একটি item মুছে ফেলে।
# __call__: object কে function হিসেবে কল করতে দেয়।
# __enter__ and __exit__: context management (with statement) এর জন্য ব্যবহৃত হয়।
# __iter__ and __next__: object কে iterator হিসেবে ব্যবহৃত করার জন্য।


# magic_methods.py

# ------------- Magic Methods in Python -------------------

# Magic methods are special methods with double underscores at the beginning and end of their names.
# They are used to define how objects of a class behave with built-in operations and functions.

# 1. __init__(self, ...) : Initialization Method
# --------------------------------------
# এটি কনস্ট্রাক্টর হিসেবে কাজ করে, এবং object তৈরি হওয়ার সময় স্বয়ংক্রিয়ভাবে কল হয়।

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

# Example usage
p = Person("Robius", 30)
print(p)  # Output: Robius, 30 years old

# 2. __str__(self) : String Representation
# --------------------------------------
# এই মেথডটি object কে string হিসেবে প্রিন্ট করার সময় ব্যবহৃত হয়।

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

# Example usage
p = Person("Robius", 30)
print(p)  # Output: Name: Robius, Age: 30

# 3. __repr__(self) : Official String Representation
# --------------------------------------
# এটি object-এর একটি আনুষ্ঠানিক string রিপ্রেজেন্টেশন প্রদান করে। সাধারণত এটি ডিবাগিংয়ের জন্য ব্যবহৃত হয়।

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"

# Example usage
p = Person("Robius", 30)
print(repr(p))  # Output: Person(name='Robius', age=30)

# 4. __len__(self) : Length of Object
# --------------------------------------
# এটি object-এর length বা সংখ্যা রিটার্ন করে। এটি list, string ইত্যাদি container type-এর length জানাতে ব্যবহৃত হয়।

class MyList:
    def __init__(self, *args):
        self.items = list(args)

    def __len__(self):
        return len(self.items)

# Example usage
lst = MyList(1, 2, 3, 4)
print(len(lst))  # Output: 4

# 5. __add__(self, other) : Addition
# --------------------------------------
# এটি দুটি object-এর মধ্যে যোগফল নির্ধারণ করে।

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Example usage
p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)  # Output: Point(4, 6)

# 6. __eq__(self, other) : Equality Comparison
# --------------------------------------
# এটি দুটি object-এর সমতা নির্ধারণ করে।

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

# Example usage
p1 = Person("Robius", 30)
p2 = Person("Robius", 30)
p3 = Person("Sani", 25)
print(p1 == p2)  # Output: True
print(p1 == p3)  # Output: False

# 7. __getitem__(self, key) : Get Item
# --------------------------------------
# এটি একটি object থেকে একটি item আনার জন্য ব্যবহৃত হয়।

class MyDict:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data.get(key, "Not found")

    def __setitem__(self, key, value):
        self.data[key] = value

# Example usage
d = MyDict()
d["name"] = "Robius"
print(d["name"])  # Output: Robius
print(d["age"])   # Output: Not found

# 8. __setitem__(self, key, value) : Set Item
# --------------------------------------
# এটি একটি item সেট করার জন্য ব্যবহৃত হয়।

class MyDict:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data.get(key, "Not found")

    def __setitem__(self, key, value):
        self.data[key] = value

# Example usage
d = MyDict()
d["name"] = "Robius"
print(d["name"])  # Output: Robius

# 9. __delitem__(self, key) : Delete Item
# --------------------------------------
# এটি একটি item মুছে ফেলার জন্য ব্যবহৃত হয়।

class MyDict:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data.get(key, "Not found")

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        if key in self.data:
            del self.data[key]

# Example usage
d = MyDict()
d["name"] = "Robius"
del d["name"]
print(d["name"])  # Output: Not found

# 10. __call__(self, ...) : Callable Objects
# --------------------------------------
# এটি একটি object কে function হিসেবে কল করার জন্য ব্যবহৃত হয়।

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

# Example usage
mul = Multiplier(3)
print(mul(5))  # Output: 15

# 11. __enter__ and __exit__ : Context Management
# --------------------------------------
# এটি context manager তৈরি করার জন্য ব্যবহৃত হয়, যেমন with statement-এর জন্য।

class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

# Example usage
with MyContextManager() as cm:
    print("Inside the context")

# Output:
# Entering the context
# Inside the context
# Exiting the context

# 12. __iter__ and __next__ : Iterator Protocol
# --------------------------------------
# এটি একটি object কে iterator হিসেবে ব্যবহৃত করার জন্য ব্যবহৃত হয়।

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Example usage
for num in Counter(1, 3):
    print(num)

# Output:
# 1
# 2
# 3
