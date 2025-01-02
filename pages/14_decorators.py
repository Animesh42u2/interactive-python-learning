import streamlit as st

# Page Title
st.title("Understanding Python Decorators 🎨")
st.markdown("""
Decorators are a powerful and flexible way to modify the behavior of functions or classes in Python.  
They are widely used in Python frameworks like Flask, Django, and more. Let’s dive in and make decorators fun and interactive! 🚀
""")

# Section 1: Introduction to Decorators
st.markdown("## 🔹 What Are Decorators?")
st.write("""
A **decorator** is a function that modifies another function or class.  
They are often used to enhance functionality, such as logging, enforcing access control, or memoization.
""")

st.markdown("### Syntax:")
st.code("""
@decorator
def function():
    pass

# Equivalent to:
function = decorator(function)
""")

# Section 2: Function Decorators
st.markdown("## 🔹 Function Decorators")
st.write("""
Function decorators take a function as input and return a modified or enhanced version of it.  
They are widely used to add logging, authentication, timing, etc.
""")

st.markdown("### Example: A Logging Decorator")
st.code("""
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished")
        return result
    return wrapper

@log_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
""")

# Interactive Example: Log Decorator
st.markdown("### 🧪 Try It: Add Logging to a Function")
name = st.text_input("Enter your name:", "Streamlit User")

def log_decorator(func):
    def wrapper(*args, **kwargs):
        st.write(f"📜 Calling `{func.__name__}`...")
        result = func(*args, **kwargs)
        st.write(f"✅ `{func.__name__}` finished.")
        return result
    return wrapper

@log_decorator
def greet(name):
    st.write(f"Hello, {name}!")

if st.button("Run Greeting Function"):
    greet(name)

# Section 3: Class Decorators
st.markdown("## 🔹 Class Decorators")
st.write("""
Class decorators modify or enhance the behavior of classes.  
They are similar to function decorators but operate at the class level.
""")

st.markdown("### Example:")
st.code("""
def class_logger(cls):
    class Wrapped(cls):
        def __init__(self, *args, **kwargs):
            print(f"Creating instance of {cls.__name__}")
            super().__init__(*args, **kwargs)
    return Wrapped

@class_logger
class Animal:
    def __init__(self, name):
        self.name = name

dog = Animal("Buddy")
""")

# Interactive Example: Class Decorator
st.markdown("### 🧪 Try It: Class Decorator")
class_logger_code = """
def class_logger(cls):
    class Wrapped(cls):
        def __init__(self, *args, **kwargs):
            st.write(f"🐾 Creating instance of `{cls.__name__}`...")
            super().__init__(*args, **kwargs)
    return Wrapped
"""

exec(class_logger_code, globals())

@class_logger
class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

species = st.text_input("Enter the animal species:", "Dog")
animal_name = st.text_input("Enter the animal name:", "Buddy")
if st.button("Create Animal"):
    animal = Animal(species, animal_name)
    st.write(f"Created Animal: `{animal.species}` named `{animal.name}`.")

# Section 4: Built-in Decorators (`@staticmethod`, `@classmethod`, `@property`)
st.markdown("## 🔹 Built-in Decorators")
st.write("""
Python provides some built-in decorators for common tasks:
- **`@staticmethod`**: Defines a method that doesn't access the class or instance.
- **`@classmethod`**: Defines a method that operates on the class level.
- **`@property`**: Defines a method that behaves like an attribute.
""")

st.markdown("### Example:")
st.code("""
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius**2

    @staticmethod
    def describe():
        return "This class represents a circle."

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)
""")

# Interactive Example: Special Decorators
st.markdown("### 🧪 Try It: Work with Circle Class")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius**2

    @staticmethod
    def describe():
        return "This class represents a circle."

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

radius = st.number_input("Enter the circle's radius:", value=5)
circle = Circle(radius)
st.write(f"Circle's Area: {circle.area}")

diameter = st.number_input("Enter the circle's diameter:", value=10)
circle_from_diameter = Circle.from_diameter(diameter)
st.write(f"Circle with Diameter `{diameter}` has Radius: `{circle_from_diameter.radius}`")

# Section 5: Combining Decorators
st.markdown("## 🔹 Combining Decorators")
st.write("""
You can stack multiple decorators on a single function. The decorators are applied in order, from the bottom up.
""")

st.markdown("### Example:")
st.code("""
def decorator_one(func):
    def wrapper(*args, **kwargs):
        print("Decorator One")
        return func(*args, **kwargs)
    return wrapper

def decorator_two(func):
    def wrapper(*args, **kwargs):
        print("Decorator Two")
        return func(*args, **kwargs)
    return wrapper

@decorator_one
@decorator_two
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
""")

# Section 6: Quiz
st.markdown("## 🎮 Quiz: Test Your Knowledge!")
quiz_question = st.radio(
    "What does the `@staticmethod` decorator do?",
    [
        "Converts a method into a static method.",
        "Converts a method into a class method.",
        "Makes a method behave like an attribute.",
        "Adds logging to a method."
    ]
)
if st.button("Submit Quiz Answer"):
    if quiz_question == "Converts a method into a static method.":
        st.success("🎉 Correct! `@staticmethod` defines a method that doesn’t access instance or class data.")
    else:
        st.error("❌ Incorrect. The correct answer is: 'Converts a method into a static method.'")

# Section 7: Summary
st.markdown("## 📚 Summary")
summary_table = {
    "Decorator": ["Function Decorator", "Class Decorator", "@staticmethod", "@classmethod", "@property"],
    "Purpose": [
        "Enhances a function’s behavior.",
        "Modifies a class’s behavior.",
        "Defines a method independent of instance or class.",
        "Defines a method that operates on the class level.",
        "Converts a method into a read-only attribute."
    ]
}
st.table(summary_table)

# Footer
st.markdown("""
---
Made with ❤️ to help you master **Decorators in Python**.  
Happy coding and exploring! 🚀
""")
