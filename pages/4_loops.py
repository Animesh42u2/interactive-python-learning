import streamlit as st
import pandas as pd

# Page Title
st.title("Loops🔄")

# Introduction
st.markdown("""
Loops allow us to execute a block of code repeatedly, saving time and reducing redundancy.  
In Python, we primarily use two types of loops: **`for` loops** and **`while` loops**.  
Let's explore how loops make our lives easier! 🚀
""")

# Section 1: What Are Loops?
st.markdown("## 🔍 What Are Loops?")
st.write("""
Loops are used to repeat a block of code until a condition is met. They are incredibly useful for tasks like:
- Iterating over a list, tuple, or dictionary.
- Performing repetitive calculations.
- Automating repetitive tasks.

In Python, we have:
1. **`for` loops**: Used to iterate over a sequence (like a list, tuple, or string).
2. **`while` loops**: Used to repeat as long as a condition is `True`.
""")

# `for` Loop Basics
st.markdown("### 🔹 `for` Loop Basics")
st.write("The syntax of a `for` loop is:")
st.code("""
for element in iterable:
    # Code to execute for each element
""")

# Interactive Example: Iterating Over a List
st.markdown("#### 🧪 Try It: Iterate Over a List")
fruits = ["apple", "banana", "cherry"]
st.write("The list of fruits: ", fruits)

if st.button("Run `for` Loop"):
    for fruit in fruits:
        st.write(f"I love {fruit}! 🍎🍌🍒")

st.code("""
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I love {fruit}!")
""")

# `while` Loop Basics
st.markdown("### 🔹 `while` Loop Basics")
st.write("The syntax of a `while` loop is:")
st.code("""
while condition:
    # Code to execute while the condition is True
""")

# Interactive Example: Counting with a `while` Loop
st.markdown("#### 🧪 Try It: Count with a `while` Loop")
max_count = st.slider("Set the maximum count:", min_value=1, max_value=10, value=5)

if st.button("Run `while` Loop"):
    count = 1
    while count <= max_count:
        st.write(f"Count: {count} 🔢")
        count += 1

st.code("""
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1
""")

# Section 2: Nested Loops
st.markdown("## 🔄 Nested Loops")
st.write("""
**Nested loops** are loops within loops. They are useful for tasks like iterating over a grid or a matrix.
""")

# Interactive Example: Multiplication Table
st.markdown("### 🧪 Try It: Multiplication Table")
num = st.number_input("Enter a number for the multiplication table:", min_value=1, value=5)

if st.button("Generate Table"):
    st.write(f"Multiplication Table for {num}:")
    table = []
    for i in range(1, 11):
        result = num * i
        table.append((num, i, result))
    table_df = pd.DataFrame(table, columns=["Number", "Multiplier", "Result"])
    st.table(table_df)

st.code("""
num = 5
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")
""")

# Section 3: Loop Control Statements
st.markdown("## 🚦 Loop Control Statements")
st.write("""
Python provides control statements to alter the flow of loops:
1. **`break`**: Exits the loop immediately.
2. **`continue`**: Skips the rest of the current iteration.
3. **`pass`**: Does nothing and moves to the next iteration.
""")

# Interactive Example: Using `break`
st.markdown("### 🛑 Using `break`")
break_limit = st.slider("Set the break limit:", min_value=1, max_value=10, value=5)

if st.button("Run `break` Example"):
    for i in range(1, 11):
        if i == break_limit:
            st.write(f"Breaking the loop at {i} 🚫")
            break
        st.write(f"Number: {i}")

st.code("""
for i in range(1, 11):
    if i == 5:
        break
    print(i)
""")

# Interactive Example: Using `continue`
st.markdown("### ➡️ Using `continue`")
skip_number = st.slider("Set a number to skip:", min_value=1, max_value=10, value=5)

if st.button("Run `continue` Example"):
    for i in range(1, 11):
        if i == skip_number:
            st.write(f"Skipping {i} ↩️")
            continue
        st.write(f"Number: {i}")

st.code("""
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
""")

# Section 4: Real-World Example
st.markdown("## 🌍 Real-World Example: FizzBuzz Game")
st.write("""
The **FizzBuzz** game is a popular coding challenge:  
- Print **Fizz** for multiples of 3.  
- Print **Buzz** for multiples of 5.  
- Print **FizzBuzz** for multiples of both 3 and 5.  
- Otherwise, print the number.
""")

if st.button("Play FizzBuzz"):
    for i in range(1, 21):
        if i % 3 == 0 and i % 5 == 0:
            st.write("FizzBuzz 🥤")
        elif i % 3 == 0:
            st.write("Fizz 🍹")
        elif i % 5 == 0:
            st.write("Buzz 🍺")
        else:
            st.write(i)

st.code("""
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
""")

# Quiz: Test Your Knowledge
st.markdown("## 🎮 Quiz: Test Your Knowledge!")
quiz_question = st.radio(
    "What does this loop output?",
    options=["1, 2, 3, 4, 5", "1, 2, 3", "Infinite Loop"],
    key="quiz_question"
)
st.code("""
count = 1
while count <= 3:
    print(count)
    count += 1
""")

if st.button("Submit Quiz Answer"):
    if quiz_question == "1, 2, 3":
        st.success("🎉 Correct! Well done.")
    else:
        st.error("❌ Incorrect. The correct answer is '1, 2, 3'.")

# Summary Table of Loops
st.markdown("## 📚 Summary of Loops")
summary_table = pd.DataFrame({
    "Loop Type": ["`for` Loop", "`while` Loop"],
    "Use Case": [
        "Iterates over a sequence (e.g., list, tuple, string).",
        "Repeats until a condition becomes `False`."
    ],
    "Example": [
        "for x in range(5): print(x)",
        "while x < 5: x += 1"
    ]
})
st.table(summary_table)

# Footer
st.markdown("""
---
Made with ❤️ to help you master loops in Python.  
Keep looping through knowledge! 🔄
""")
