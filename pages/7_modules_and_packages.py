import streamlit as st
import math
import random
import os
import sys
import pandas as pd

# Page Title
st.title("All About Modules and Packages in Python 📦")

st.markdown("""
Modules and packages are essential in Python for organizing code, reusing functionality, and accessing a rich ecosystem of libraries.  
Let’s dive into the world of **modules and packages** and explore how they simplify programming! 🚀  
""")

# Section 1: What Are Modules?
st.markdown("## 🔹 What Are Modules?")
st.write("""
A **module** is a file containing Python code (functions, classes, variables).  
Modules allow us to organize and reuse code across multiple files or projects.  
""")

st.markdown("### Example:")
st.code("""
# Importing a built-in module
import math

# Using a function from the math module
result = math.sqrt(16)
print(result)  # Output: 4.0
""")

# Interactive Example: Using the `math` Module
st.markdown("### 🧪 Try It: Use the `math` Module")
number = st.number_input("Enter a number to find its square root:", min_value=0.0, value=16.0)
st.write(f"The square root of {number} is: `{math.sqrt(number)}`")

# Section 2: Creating Custom Modules
st.markdown("## 🔹 Creating Custom Modules")
st.write("""
You can create your own module by saving Python code in a `.py` file.  
Here’s an example of a custom module called `greetings.py`:
""")

st.code("""
# greetings.py
def greet(name):
    return f"Hello, {name}!"

# Importing and using the custom module
import greetings
print(greetings.greet("Python"))  # Output: Hello, Python!
""")

st.markdown("### Interactive Task:")
st.write("Imagine you've created a custom module named `greetings`. Try using it in your project!")

# Section 3: Standard Library Modules
st.markdown("## 🔹 Standard Library Modules")
st.write("""
Python comes with a rich standard library of modules. Let’s explore some popular ones:  
""")

# Subsection: `math` Module
st.markdown("### 🔸 `math` Module")
st.write("""
The `math` module provides mathematical functions like `sqrt()`, `sin()`, and constants like `pi`.
""")
st.markdown("#### Example:")
st.code("""
import math
print(math.pi)  # Output: 3.141592653589793
""")
st.write(f"The value of `pi` is: `{math.pi}`")

# Subsection: `random` Module
st.markdown("### 🔸 `random` Module")
st.write("""
The `random` module is used for generating random numbers, selecting random items, and more.
""")
st.markdown("#### Example:")
st.code("""
import random
print(random.randint(1, 10))  # Output: A random number between 1 and 10
""")

# Interactive Example: Generate Random Numbers
st.markdown("### 🧪 Try It: Generate a Random Number")
start = st.number_input("Enter the start of the range:", value=1)
end = st.number_input("Enter the end of the range:", value=10)
if st.button("Generate Random Number"):
    st.write(f"Random Number: `{random.randint(start, end)}`")

# Subsection: `os` Module
st.markdown("### 🔸 `os` Module")
st.write("""
The `os` module provides functions to interact with the operating system.
""")
st.markdown("#### Example:")
st.code("""
import os
print(os.getcwd())  # Output: Current working directory
""")
st.write(f"Your current working directory is: `{os.getcwd()}`")

# Subsection: `sys` Module
st.markdown("### 🔸 `sys` Module")
st.write("""
The `sys` module provides access to system-specific parameters and functions.
""")
st.markdown("#### Example:")
st.code("""
import sys
print(sys.version)  # Output: Python version
""")
st.write(f"Your Python version is: `{sys.version}`")

# Section 4: Installing Packages
st.markdown("## 🔹 Installing Packages")
st.write("""
You can install external packages using **pip**, Python's package manager.
""")
st.markdown("#### Example:")
st.code("""
# Installing a package (e.g., pandas)
pip install pandas
""")

st.write("""
After installation, you can use the package in your project:
""")
st.code("""
import pandas as pd
df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})
print(df)
""")

# Section 5: Organizing Code with Packages
st.markdown("## 🔹 Organizing Code with Packages")
st.write("""
A **package** is a collection of modules organized in directories with an `__init__.py` file.  
It allows you to structure your project into smaller, manageable parts.  
""")

st.markdown("### Example:")
st.code("""
# Project structure:
# my_package/
# ├── __init__.py
# ├── module1.py
# └── module2.py

# Importing from a package
from my_package.module1 import my_function
my_function()
""")

# Section 6: Quiz
st.markdown("## 🎮 Quiz: Test Your Knowledge")
quiz_question = st.radio(
    "What does the following code do?",
    options=[
        "Imports the `sqrt` function from the `math` module.",
        "Calculates the square root of a number.",
        "Imports the `math` module."
    ]
)
st.code("""
from math import sqrt
""")

if st.button("Submit Quiz Answer"):
    if quiz_question == "Imports the `sqrt` function from the `math` module.":
        st.success("🎉 Correct! The code imports only the `sqrt` function from the `math` module.")
    else:
        st.error("❌ Incorrect. The correct answer is: 'Imports the `sqrt` function from the `math` module.'")

# Section 7: Summary
st.markdown("## 📚 Summary")
summary_table = pd.DataFrame({
    "Topic": [
        "Importing Modules", "Creating Custom Modules", 
        "Standard Library Modules", "Installing Packages", "Packages"
    ],
    "Description": [
        "Use `import` to access functionality from other Python files.",
        "Create your own reusable `.py` files.",
        "Explore built-in modules like `os`, `math`, `random`, and `sys`.",
        "Install third-party libraries using `pip`.",
        "Organize your project into directories with modules."
    ]
})
st.table(summary_table)

# Footer
st.markdown("""
---
Made with ❤️ to help you understand **Modules and Packages** in Python.  
Happy Coding! 🚀  
""")
