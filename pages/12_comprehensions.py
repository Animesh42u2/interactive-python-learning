import streamlit as st

# Page Title
st.title("Master Python Comprehensions 🎨")
st.markdown("""
Python comprehensions are a concise way to create lists, dictionaries, sets, and generators.  
They make your code cleaner, more efficient, and easier to read. Let’s explore comprehensions interactively! 🚀
""")

# Section 1: What Are Comprehensions?
st.markdown("## 🔹 What Are Comprehensions?")
st.write("""
Comprehensions are constructs in Python that allow you to create new collections (like lists or dictionaries) in a single line of code.  
They are compact, expressive, and often faster than loops.
""")

st.markdown("### Why Use Comprehensions?")
st.write("""
- **Compact Code**: Create collections in one line.
- **Performance**: Comprehensions are optimized for Python’s internals.
- **Readability**: They make intentions clear to readers.
""")

# Section 2: List Comprehensions
st.markdown("## 🔹 List Comprehensions")
st.write("""
List comprehensions are a concise way to create lists. The syntax is:  
`[expression for item in iterable if condition]`
""")

st.markdown("### Example:")
st.code("""
# Without list comprehension
squares = []
for i in range(10):
    squares.append(i**2)

# With list comprehension
squares = [i**2 for i in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
""")

# Interactive Example: Generate a List of Squares
st.markdown("### 🧪 Try It: Generate a List of Squares")
n = st.number_input("Enter the range of numbers:", min_value=1, value=10)
squares = [i**2 for i in range(n)]
st.write(f"Squares: {squares}")

# Section 3: Dictionary Comprehensions
st.markdown("## 🔹 Dictionary Comprehensions")
st.write("""
Dictionary comprehensions are used to create dictionaries in a compact way. The syntax is:  
`{key_expression: value_expression for item in iterable if condition}`
""")

st.markdown("### Example:")
st.code("""
# Without dictionary comprehension
num_dict = {}
for i in range(5):
    num_dict[i] = i**2

# With dictionary comprehension
num_dict = {i: i**2 for i in range(5)}
print(num_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
""")

# Interactive Example: Generate a Dictionary of Squares
st.markdown("### 🧪 Try It: Create a Dictionary of Squares")
num_dict = {i: i**2 for i in range(n)}
st.write(f"Number Dictionary: {num_dict}")

# Section 4: Set Comprehensions
st.markdown("## 🔹 Set Comprehensions")
st.write("""
Set comprehensions are used to create sets in a concise manner. The syntax is:  
`{expression for item in iterable if condition}`
""")

st.markdown("### Example:")
st.code("""
# Without set comprehension
unique_squares = set()
for i in range(10):
    unique_squares.add(i**2)

# With set comprehension
unique_squares = {i**2 for i in range(10)}
print(unique_squares)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
""")

# Interactive Example: Generate a Set of Unique Squares
st.markdown("### 🧪 Try It: Create a Set of Unique Squares")
unique_squares = {i**2 for i in range(n)}
st.write(f"Unique Squares Set: {unique_squares}")

# Section 5: Generator Expressions
st.markdown("## 🔹 Generator Expressions")
st.write("""
Generator expressions are like comprehensions but for generating values lazily (one at a time).  
They use `()` instead of `[]` or `{}`. The syntax is:  
`(expression for item in iterable if condition)`
""")

st.markdown("### Example:")
st.code("""
# Without generator expression
def generate_squares(n):
    for i in range(n):
        yield i**2

# With generator expression
squares_gen = (i**2 for i in range(10))
print(list(squares_gen))  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
""")

# Interactive Example: Generate Squares Lazily
st.markdown("### 🧪 Try It: Use a Generator Expression")
squares_gen = (i**2 for i in range(n))
st.write("Generated Values:")
for _ in range(n):
    st.write(next(squares_gen))

# Section 6: Nested Comprehensions
st.markdown("## 🔹 Nested Comprehensions")
st.write("""
Comprehensions can be nested for more complex operations.  
For example, creating a multiplication table using nested comprehensions:
""")
st.code("""
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print(table)  # Output: Multiplication table from 1 to 5
""")

# Interactive Example: Multiplication Table
st.markdown("### 🧪 Try It: Generate a Multiplication Table")
table_size = st.number_input("Enter table size:", min_value=1, value=5)
multiplication_table = [[i * j for j in range(1, table_size + 1)] for i in range(1, table_size + 1)]
st.write("Multiplication Table:")
st.table(multiplication_table)

# Section 7: Quiz
st.markdown("## 🎮 Quiz: Test Your Knowledge!")
quiz_question = st.radio(
    "What does this list comprehension do?",
    options=[
        "[x for x in range(10) if x % 2 == 0]",
        "{x: x**2 for x in range(5)}",
        "(x**2 for x in range(5))"
    ]
)
st.code("""
[expression for item in iterable if condition]
""")

if st.button("Submit Quiz Answer"):
    if quiz_question == "[x for x in range(10) if x % 2 == 0]":
        st.success("🎉 Correct! This generates a list of even numbers.")
    else:
        st.error("❌ Incorrect. Try to understand the syntax again!")

# Section 8: Summary Table
st.markdown("## 📚 Summary")
summary_table = {
    "Type": ["List Comprehension", "Dictionary Comprehension", "Set Comprehension", "Generator Expression"],
    "Syntax": [
        "[expression for item in iterable]",
        "{key: value for item in iterable}",
        "{expression for item in iterable}",
        "(expression for item in iterable)"
    ],
    "Use Case": [
        "Create a new list",
        "Create a new dictionary",
        "Create a new set",
        "Generate values lazily"
    ]
}
st.table(summary_table)

# Footer
st.markdown("""
---
Made with ❤️ to help you master **Comprehensions in Python**.  
Happy coding and keep exploring! 🚀  
""")
