import streamlit as st
import pandas as pd

# Page Title
st.title("Conditional Statements 😲")

# Introduction
st.markdown("""
Conditional statements allow us to perform different actions based on conditions.  
In Python, we primarily use `if`, `elif`, and `else`.  
""")

# What Are Conditional Statements?
st.markdown("## What Are Conditional Statements?")
st.write("""
Conditional statements evaluate a condition (a boolean expression) and execute specific code blocks based on whether the condition is `True` or `False`.  
They are essential for decision-making in programs. The structure is as follows:
""")
st.code("""
if condition:
    # Code to execute if the condition is True
elif another_condition:
    # Code to execute if the first condition is False and this condition is True
else:
    # Code to execute if none of the conditions are True
""")

# Test: Check if a Number is Even or Odd
st.markdown("## 🧪 Test: Check if a Number is Even or Odd")
num = st.number_input("Enter a number to check if it's even or odd", value=0)

if num % 2 == 0:
    st.success(f"The number {num} is even. ✅")
else:
    st.error(f"The number {num} is odd. ❌")

st.markdown("**Code:**")
st.code("""
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
""")

# Advanced Example: Grade Calculator
st.markdown("## 👩‍💻 Advanced Example: Grade Calculator")
score = st.number_input("Enter your score (0-100):", min_value=0, max_value=100, value=75)

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

st.write(f"**Grade:** {grade} 🌟")
st.markdown("**Code:**")
st.code("""
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
""")

# Examples of Conditional Statements
st.markdown("## 📜 Examples of Conditional Statements")
examples_table = pd.DataFrame({
    "Condition": ["x > 5", "x == 10", "x < 0", "x % 2 == 0"],
    "Description": [
        "Checks if x is greater than 5",
        "Checks if x is exactly equal to 10",
        "Checks if x is negative",
        "Checks if x is an even number"
    ],
    "Example Input (x)": [7, 10, -1, 4],
    "Result": [True, True, True, True]
})
st.table(examples_table)

# Quiz: Test Your Knowledge
st.markdown("## 🎮 Quiz: Test Your Knowledge!")
quiz_code = """
x = 5
if x > 10:
    print("Greater than 10")
elif x == 5:
    print("Equal to 5")
else:
    print("Less than 10")
"""
st.code(quiz_code)

quiz_answer = st.radio(
    "Your Answer:",
    options=["Greater than 10", "Equal to 5", "Less than 10"]
)

if st.button("Submit Answer"):
    correct_answer = "Equal to 5"
    if quiz_answer == correct_answer:
        st.success("🎉 Correct! Great job!")
    else:
        st.error(f"❌ Incorrect. The correct answer is: {correct_answer}")

# Summary of Conditional Statements
st.markdown("## 📚 Summary of Conditional Statements")
summary_table = pd.DataFrame({
    "Statement": ["if", "elif", "else"],
    "Use": [
        "Executes a block of code if the condition is True",
        "Executes if the previous conditions are False and this one is True",
        "Executes if none of the previous conditions are True"
    ],
    "Example": [
        "if x > 10: print('Greater than 10')",
        "elif x == 10: print('Equal to 10')",
        "else: print('Less than 10')"
    ]
})
st.table(summary_table)

# Footer
st.markdown("""
---
Made with ❤️ for learners like you.  
Keep exploring and coding!
""")
