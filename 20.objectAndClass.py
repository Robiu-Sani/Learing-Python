# objects_in_python.py

# ------------------------ Object-Oriented Programming in Python ------------------------

# 1. What is an Object?
# ------------------------
# Python-এ, একটি object হল ডেটা এবং ফাংশনগুলির একটি সংমিশ্রণ, যা একটি ক্লাসের উদাহরণ।

# 2. Class and Object
# ------------------------
# Class হল একটি ব্লুপ্রিন্ট বা টেম্পলেট যা দ্বারা object তৈরি হয়। একটি class বিভিন্ন বৈশিষ্ট্য (attributes) 
# এবং পদ্ধতি (methods) সমন্বিত হয়। object হল class থেকে তৈরি কৃত একটি বাস্তব উদাহরণ।

# Class তৈরি করা:

class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."  # Method

# Object তৈরি করা:

person1 = Person("Robius", 25)
print(person1.greet())  # Output: Hello, my name is Robius and I am 25 years old.


# 3. Class Attributes and Instance Attributes
# ------------------------
# Class Attributes হল class এর জন্য সাধারণ বৈশিষ্ট্য যা সব object দ্বারা ভাগাভাগি করা হয়।
# Instance Attributes হল নির্দিষ্ট object এর জন্য বৈশিষ্ট্য যা শুধু ঐ object এর জন্য প্রযোজ্য।

class Car:
    wheels = 4  # Class Attribute

    def __init__(self, color, model):
        self.color = color  # Instance Attribute
        self.model = model  # Instance Attribute

car1 = Car("Red", "Toyota")
car2 = Car("Blue", "Honda")

print(car1.color)  # Output: Red
print(car2.color)  # Output: Blue
print(car1.wheels) # Output: 4


# 4. Methods in Classes
# ------------------------
# Methods হল class এর ভিতরে সংজ্ঞায়িত ফাংশন যা object দ্বারা অ্যাক্সেস করা যায়।
# Special Methods (Magic Methods) হল নির্দিষ্ট কাজের জন্য ব্যবহৃত পূর্বনির্ধারিত methods।

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} is barking."

    def __str__(self):
        return f"{self.name} is a {self.breed}."

dog1 = Dog("Max", "Golden Retriever")
print(dog1.bark())  # Output: Max is barking.
print(dog1)         # Output: Max is a Golden Retriever.


# 5. Inheritance
# ------------------------
# Inheritance হল একটি class অন্য একটি class এর বৈশিষ্ট্য এবং পদ্ধতিগুলি উত্তরাধিকার সূত্রে গ্রহণ করা।

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal Sound"

class Cat(Animal):
    def speak(self):
        return "Meow"

cat1 = Cat("Whiskers")
print(cat1.name)    # Output: Whiskers
print(cat1.speak()) # Output: Meow


# 6. Encapsulation
# ------------------------
# Encapsulation হল object এর ডেটাকে লুকানো (hide) এবং কেবলমাত্র class এর ভিতরে অ্যাক্সেস করার পদ্ধতি।
# Private Attributes/Pubilc Attributes দ্বারা এটি করা হয়।

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner       # Public Attribute
        self.__balance = balance # Private Attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.__balance

account = BankAccount("Robius", 1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
account.withdraw(2000)        # Output: Insufficient funds


# 7. Polymorphism
# ------------------------
# Polymorphism হল একই ইন্টারফেস বা মেথড বিভিন্ন ধরনের class দ্বারা বাস্তবায়িত করা।

class Bird:
    def fly(self):
        return "Bird is flying"

class Airplane:
    def fly(self):
        return "Airplane is flying"

# Polymorphism in action:
def lift_off(entity):
    print(entity.fly())

bird = Bird()
airplane = Airplane()

lift_off(bird)      # Output: Bird is flying
lift_off(airplane)  # Output: Airplane is flying


# 8. Abstract Classes and Interfaces
# ------------------------
# Abstract Classes এমন এক ধরনের class যা সম্পূর্ণ হয় না এবং এটি শুধু ব্লুপ্রিন্ট দেয়।
# Abstract Class থেকে ডিরাইভড ক্লাসগুলো সেই ব্লুপ্রিন্টের ভিত্তিতে কাজ সম্পূর্ণ করে।

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(10, 5)
print("Rectangle Area:", rect.area())  # Output: Rectangle Area: 50


# 9. Object-Oriented Design Principles
# ------------------------
# SOLID হল Object-Oriented Design এর পাঁচটি প্রধান নীতি:
# 1. S - Single Responsibility Principle
# 2. O - Open/Closed Principle
# 3. L - Liskov Substitution Principle
# 4. I - Interface Segregation Principle
# 5. D - Dependency Inversion Principle


# 10. Advanced Concepts: Metaclasses
# ------------------------
# Metaclass হল class এর ক্লাস। এটি class তৈরি এবং সংশোধন করতে ব্যবহৃত হয়।

class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)

class CustomClass(metaclass=Meta):
    pass

# Output: Creating class CustomClass


# ------------------------ End of the Python file ------------------------
# inheritance.py

# ------------- Inheritance in Python -------------------

# Inheritance একটি OOP (Object-Oriented Programming) concept, যা parent (বা base) class-এর property এবং methods child (বা derived) class-এ inherit করতে দেয়।

# 1. Basic Inheritance
# -----------------------
# নিচের উদাহরণে, `Person` হলো parent class এবং `Student` হলো child class।

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# `Student` class `Person` class থেকে Inherit করেছে।
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Parent class-এর __init__ মেথডকে কল করা হচ্ছে
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying."

# Example usage
s = Student("Robius", 20, "S1234")
print(s.greet())  # Output: Hello, my name is Robius and I am 20 years old.
print(s.study())  # Output: Robius is studying.

# 2. Overriding Methods
# -----------------------
# Child class তার parent class-এর method-কে override করতে পারে।

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    # greet() মেথডটি override করা হয়েছে
    def greet(self):
        return f"Hi, I'm {self.name}, and I'm a student with ID: {self.student_id}"

# Example usage
s = Student("Robius", 20, "S1234")
print(s.greet())  # Output: Hi, I'm Robius, and I'm a student with ID: S1234

# 3. Multiple Inheritance
# -----------------------
# Python-এ একাধিক parent class থেকে inherit করা যায়।

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

class Worker:
    def __init__(self, job_title):
        self.job_title = job_title

    def work(self):
        return f"I work as a {self.job_title}."

# `Employee` class, `Person` এবং `Worker` দুটি class থেকে inherit করেছে।
class Employee(Person, Worker):
    def __init__(self, name, age, job_title):
        Person.__init__(self, name, age)
        Worker.__init__(self, job_title)

# Example usage
e = Employee("Robius", 30, "Software Developer")
print(e.greet())  # Output: Hello, my name is Robius and I am 30 years old.
print(e.work())   # Output: I work as a Software Developer.

# 4. The `super()` Function
# -----------------------
# `super()` function Parent class-এর কোনো method বা attribute কে Child class থেকে access করার জন্য ব্যবহৃত হয়।

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # `super()` দিয়ে Parent class এর __init__ মেথড কল করা হয়েছে
        self.student_id = student_id

    def greet(self):
        parent_greet = super().greet()  # Parent class এর greet মেথড ব্যবহার করে
        return f"{parent_greet} I am a student with ID: {self.student_id}."

# Example usage
s = Student("Robius", 20, "S1234")
print(s.greet())  # Output: Hello, my name is Robius and I am 20 years old. I am a student with ID: S1234.

# 5. Inheritance Hierarchy
# -----------------------
# Inheritance-এ একটি class অন্য class থেকে inherit করতে পারে, যা একটি শ্রেণিবদ্ধ কাঠামো তৈরি করে।

class Animal:
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Bulldog(Dog):
    def sound(self):
        return "Bulldog Bark"

# Example usage
dog = Dog()
bulldog = Bulldog()
print(dog.sound())      # Output: Bark
print(bulldog.sound())  # Output: Bulldog Bark

# 6. Checking Inheritance with `isinstance()` and `issubclass()`
# -----------------------
# `isinstance()` দিয়ে কোনো object নির্দিষ্ট class-এর instance কিনা চেক করা হয়।
# `issubclass()` দিয়ে কোনো class নির্দিষ্ট অন্য class-এর subclass কিনা চেক করা হয়।

class Animal:
    pass

class Dog(Animal):
    pass

d = Dog()
print(isinstance(d, Dog))        # Output: True
print(isinstance(d, Animal))     # Output: True
print(issubclass(Dog, Animal))   # Output: True
print(issubclass(Animal, Dog))   # Output: False
