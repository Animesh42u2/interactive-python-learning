import streamlit as st

# Page Title
st.title("Dive into Object-Oriented Programming (OOP) in Python 🏛️")

st.markdown("""
Object-Oriented Programming (OOP) is a programming paradigm that represents concepts as **objects**.  
It’s a fantastic way to model real-world problems in Python. Let's explore OOP interactively! 🚀
""")

# Section 1: Classes and Objects
st.markdown("## 🔹 Classes and Objects")
st.write("""
A **class** is like a blueprint, while an **object** is an instance of that blueprint.  
For example, a `Car` class could have objects like `Car('Toyota')` or `Car('Honda')`.
""")

st.markdown("### Example:")
st.code("""
class Car:
    def __init__(self, brand):
        self.brand = brand

my_car = Car("Toyota")
print(my_car.brand)  # Output: Toyota
""")

# Interactive Example: Creating a Class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        return f"The {self.brand} {self.model} is driving!"

st.markdown("### 🧪 Try It: Create a Car")
car_brand = st.text_input("Enter the car brand:", "Toyota")
car_model = st.text_input("Enter the car model:", "Corolla")
my_car = Car(car_brand, car_model)
st.write(my_car.drive())

# Section 2: Instance and Class Variables
st.markdown("## 🔹 Instance and Class Variables")
st.write("""
- **Instance Variables**: Belong to the object and can vary between instances.
- **Class Variables**: Shared across all instances of the class.
""")

st.markdown("### Example:")
st.code("""
class Dog:
    species = "Canis lupus familiaris"  # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

dog1 = Dog("Buddy")
dog2 = Dog("Max")
print(dog1.species, dog2.species)  # Both share the same class variable
print(dog1.name, dog2.name)  # Different instance variables
""")

# Interactive Example: Dogs
class Dog:
    species = "Canis lupus familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

dog_name = st.text_input("Enter your dog's name:", "Buddy")
dog_age = st.number_input("Enter your dog's age:", value=3, min_value=0)
dog = Dog(dog_name, dog_age)
st.write(f"Your dog, {dog.name}, is {dog.age} years old and belongs to the species {dog.species}.")

# Section 3: Methods and Class Methods
st.markdown("## 🔹 Methods and Class Methods")
st.write("""
- **Instance Methods**: Operate on an object’s instance variables.
- **Class Methods**: Operate on class-level variables, defined with `@classmethod`.
- **Static Methods**: Do not operate on instance or class variables, defined with `@staticmethod`.
""")

st.markdown("### Example:")
st.code("""
class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def info(cls):
        return "This is a Math class."

print(Math.add(2, 3))  # Output: 5
print(Math.info())  # Output: This is a Math class.
""")

# Interactive Example: Static and Class Methods
class Math:
    @staticmethod
    def multiply(a, b):
        return a * b

    @classmethod
    def class_info(cls):
        return "This is a Math utility class."

num1 = st.number_input("Enter the first number:", value=2)
num2 = st.number_input("Enter the second number:", value=3)
st.write(f"The product is: {Math.multiply(num1, num2)}")
st.write(Math.class_info())

# Section 4: Inheritance and Polymorphism
st.markdown("## 🔹 Inheritance and Polymorphism")
st.write("""
- **Inheritance**: Allows a class (child) to inherit properties and methods from another class (parent).
- **Polymorphism**: Allows methods to have different behavior depending on the object calling them.
""")

st.markdown("### Example:")
st.code("""
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Different behavior for the same method
""")

# Interactive Example: Polymorphism
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for animal in animals:
    st.write(animal.speak())

# Section 5: Encapsulation and Abstraction
st.markdown("## 🔹 Encapsulation and Abstraction")
st.write("""
- **Encapsulation**: Restricts access to certain attributes using private variables (`__variable`).
- **Abstraction**: Hides implementation details, exposing only the essential features.
""")

st.markdown("### Example:")
st.code("""
class BankAccount:
    def __init__(self, owner, balance):
        self.__balance = balance  # Private variable
        self.owner = owner

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

account = BankAccount("Alice", 100)
account.deposit(50)
print(account.__balance)  # Error: Cannot access private variable
""")

# Interactive Example: Bank Account
class BankAccount:
    def __init__(self, owner, balance):
        self.__balance = balance
        self.owner = owner

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds"
        self.__balance -= amount
        return f"New balance: {self.__balance}"

account_owner = st.text_input("Enter account owner's name:", "Alice")
initial_balance = st.number_input("Enter initial balance:", value=100, min_value=0)
account = BankAccount(account_owner, initial_balance)

deposit_amount = st.number_input("Enter deposit amount:", value=50, min_value=0)
if st.button("Deposit"):
    account.deposit(deposit_amount)
    st.write(f"Deposited {deposit_amount}. New balance: Hidden for encapsulation!")

withdraw_amount = st.number_input("Enter withdrawal amount:", value=30, min_value=0)
if st.button("Withdraw"):
    st.write(account.withdraw(withdraw_amount))

# Section 6: Magic Methods
st.markdown("## 🔹 Magic Methods")
st.write("""
Magic methods are special methods surrounded by double underscores (e.g., `__init__`, `__str__`) that define specific behaviors.
""")

st.markdown("### Example:")
st.code("""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

book = Book("1984", "George Orwell")
print(book)  # Output: 1984 by George Orwell
""")

# Interactive Example: Magic Method
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

book_title = st.text_input("Enter book title:", "1984")
book_author = st.text_input("Enter author name:", "George Orwell")
book = Book(book_title, book_author)
st.write(book)

# Section 7: Quiz
st.markdown("## 🎮 Quiz: Test Your OOP Knowledge")
quiz_question = st.radio(
    "What is the purpose of the `__init__` method?",
    ["To initialize an object’s attributes", "To destroy an object", "To create a class"],
)
if st.button("Submit Answer"):
    if quiz_question == "To initialize an object’s attributes":
        st.success("🎉 Correct! The `__init__` method initializes attributes of a class.")
    else:
        st.error("❌ Incorrect. The correct answer is: 'To initialize an object’s attributes'.")

# Footer
st.markdown("""
---
Made with ❤️ to help you master **Object-Oriented Programming** in Python.  
Keep coding and exploring! 🚀
""")
