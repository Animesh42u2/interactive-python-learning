import streamlit as st
import pandas as pd

# Page Title
st.title("Python Syntax & Variables 🚀")

# Introduction
st.markdown("""
Welcome to a fun and interactive way to learn Python's syntax and data types!  
Dive into the details, play quizzes, and explore with examples. 🎉
""")

# Input for Name and Age
st.markdown("### Let's Start with Variables")
name = st.text_input("What's your name?", "John Doe")
age = st.number_input("What's your age?", min_value=0, value=20)

# Displaying the Inputs
st.write(f"Hello, {name}! You are {age} years old. Are you ready to explore Python? 🎉")

# Display Variables Table
variables_table = pd.DataFrame({
    "Variable": ["name", "age"],
    "Type": ["String", "Integer"],
    "Value": [name, age]
})
st.table(variables_table)

# Data Types Overview
st.markdown("## Python Data Types Overview")
data_types_table = pd.DataFrame({
    "Data Type": ["Integer (int)", "Float (float)", "String (str)", "List", "Tuple", "Set", "Dictionary (dict)", "Boolean (bool)"],
    "Type": ["Primitive", "Primitive", "Primitive", "Non-Primitive", "Non-Primitive", "Non-Primitive", "Non-Primitive", "Primitive"],
    "Mutability": ["Immutable", "Immutable", "Immutable", "Mutable", "Immutable", "Mutable", "Mutable", "Immutable"],
    "Example": [42, 3.14, '"Hello"', "[1, 2, 3]", "(1, 2, 3)", "{1, 2, 3}", "{'key': 'value'}", "True"]
})
st.dataframe(data_types_table)

# Let's Play: Guess the Data Type
st.markdown("### 🎮 Let's Play: Guess the Data Type!")
quiz_data = [
    ("42", "Integer (int)"),
    ("3.14", "Float (float)"),
    ('"Hello"', "String (str)"),
    ("[1, 2, 3]", "List"),
    ("(1, 2, 3)", "Tuple"),
    ("{1, 2, 3}", "Set"),
    ("{'key': 'value'}", "Dictionary (dict)"),
    ("True", "Boolean (bool)")
]

if "quiz_question" not in st.session_state:
    import random
    st.session_state.quiz_question = random.choice(quiz_data)

quiz_question = st.session_state.quiz_question
st.write(f"**Question:** What is the data type of this value?")
st.code(quiz_question[0])

# Answer Input
user_answer = st.selectbox(
    "Choose your answer:",
    ["Integer (int)", "Float (float)", "String (str)", "List", "Tuple", "Set", "Dictionary (dict)", "Boolean (bool)"]
)

if st.button("Submit Answer"):
    if user_answer == quiz_question[1]:
        st.success("🎉 Correct! Great job!")
    else:
        st.error(f"❌ Incorrect. The correct answer is: {quiz_question[1]}")

    # Reset for the next question
    st.session_state.quiz_question = random.choice(quiz_data)
    st.experimental_rerun()

# Explore Data Types in Detail
st.markdown("## 🔍 Explore Data Types in Detail")
selected_data_type = st.selectbox(
    "Choose a data type to explore:",
    ["int", "float", "str", "list", "tuple", "set", "dict", "bool"]
)

# Information for Each Data Type
data_type_details = {
    "int": {
        "Name": "Integer (int)",
        "Type": "Primitive",
        "Mutability": "Immutable",
        "Range": "Unlimited",
        "Description": "Whole numbers without a fractional component.",
        "Example Code": """
x = 42
y = -15
z = x + y
print(z)  # Output: 27
"""
    },
    "float": {
        "Name": "Float (float)",
        "Type": "Primitive",
        "Mutability": "Immutable",
        "Range": "Unlimited (but limited by memory)",
        "Description": "Numbers with a fractional component.",
        "Example Code": """
x = 3.14
y = 2.71
z = x * y
print(z)  # Output: 8.5094
"""
    },
    "str": {
        "Name": "String (str)",
        "Type": "Primitive",
        "Mutability": "Immutable",
        "Range": "Unlimited",
        "Description": "A sequence of characters enclosed in single or double quotes.",
        "Example Code": """
greeting = "Hello"
name = "Alice"
message = f"{greeting}, {name}!"
print(message)  # Output: Hello, Alice!
"""
    },
    "list": {
        "Name": "List",
        "Type": "Non-Primitive",
        "Mutability": "Mutable",
        "Range": "Unlimited",
        "Description": "A collection of items enclosed in square brackets.",
        "Example Code": """
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']
"""
    },
    "tuple": {
        "Name": "Tuple",
        "Type": "Non-Primitive",
        "Mutability": "Immutable",
        "Range": "Unlimited",
        "Description": "An ordered collection of items enclosed in parentheses.",
        "Example Code": """
dimensions = (1920, 1080)
width, height = dimensions
print(width, height)  # Output: 1920 1080
"""
    },
    "set": {
        "Name": "Set",
        "Type": "Non-Primitive",
        "Mutability": "Mutable (but items must be immutable)",
        "Range": "Unlimited",
        "Description": "An unordered collection of unique items.",
        "Example Code": """
unique_numbers = {1, 2, 3, 3, 2}
unique_numbers.add(4)
print(unique_numbers)  # Output: {1, 2, 3, 4}
"""
    },
    "dict": {
        "Name": "Dictionary (dict)",
        "Type": "Non-Primitive",
        "Mutability": "Mutable",
        "Range": "Unlimited",
        "Description": "A collection of key-value pairs enclosed in curly braces.",
        "Example Code": """
person = {"name": "Alice", "age": 30}
person["city"] = "New York"
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
"""
    },
    "bool": {
        "Name": "Boolean (bool)",
        "Type": "Primitive",
        "Mutability": "Immutable",
        "Range": "True or False",
        "Description": "A logical data type that can only be True or False.",
        "Example Code": """
x = True
y = False
print(x and y)  # Output: False
"""
    }
}

# Display Details
if selected_data_type in data_type_details:
    details = data_type_details[selected_data_type]
    st.markdown(f"### {details['Name']}")
    st.markdown(f"- **Type:** {details['Type']}")
    st.markdown(f"- **Mutability:** {details['Mutability']}")
    st.markdown(f"- **Range:** {details['Range']}")
    st.markdown(f"- **Description:** {details['Description']}")
    st.code(details["Example Code"])

# Summary Table
st.markdown("## 📊 Summary of Data Types")
st.write("Here's a summary table of all the data types we've explored:")
st.dataframe(data_types_table)

# Footer
st.markdown("""
---
Made with ❤️ to help you embark on your Python journey.
""")
