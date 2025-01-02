import streamlit as st

# Page Title
st.title("Mastering Iterators and Generators in Python 🔄")

st.markdown("""
Iterators and generators are powerful tools in Python for managing sequences of data efficiently.  
They allow you to process large datasets, create pipelines, and write memory-efficient code. Let’s explore! 🚀
""")

# Section 1: Iterators
st.markdown("## 🔹 What Are Iterators?")
st.write("""
An **iterator** is an object that allows you to traverse through all the elements in a collection, one at a time.  
It must implement two methods:
1. **`__iter__()`**: Returns the iterator object itself.
2. **`__next__()`**: Returns the next element or raises `StopIteration` when there are no more elements.
""")

st.markdown("### Example:")
st.code("""
# Creating an iterator
my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
""")

# Interactive Example: Create Your Iterator
st.markdown("### 🧪 Try It: Use an Iterator")
my_list = st.text_input("Enter a list of items (comma-separated):", "1, 2, 3").split(", ")
iterator = iter(my_list)

if st.button("Get Next Item"):
    try:
        next_item = next(iterator)
        st.write(f"Next item: `{next_item}`")
    except StopIteration:
        st.error("No more items in the iterator!")

# Section 2: Generators
st.markdown("## 🔹 What Are Generators?")
st.write("""
Generators are a type of iterator, but they are simpler to implement.  
Instead of returning values like a function, they use the **`yield`** keyword to produce a sequence of values.
""")

st.markdown("### Example:")
st.code("""
# Generator function
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

gen = count_up_to(5)
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
""")

# Interactive Example: Generate Numbers
st.markdown("### 🧪 Try It: Generate Numbers")
max_value = st.number_input("Enter the maximum number to generate:", value=5)

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

gen = count_up_to(max_value)
if st.button("Generate Next Number"):
    try:
        st.write(f"Generated Number: `{next(gen)}`")
    except StopIteration:
        st.error("Generator has no more values!")

# Section 3: Generator Expressions
st.markdown("## 🔹 Generator Expressions")
st.write("""
Generator expressions are a concise way to create generators. They use parentheses `()` instead of square brackets `[]` for list comprehensions.
""")

st.markdown("### Example:")
st.code("""
# Generator Expression
squares = (x**2 for x in range(5))
print(next(squares))  # Output: 0
print(next(squares))  # Output: 1
""")

# Interactive Example: Squares Generator
st.markdown("### 🧪 Try It: Generate Squares")
num = st.number_input("Enter a range for squares:", min_value=1, value=5)
squares_gen = (x**2 for x in range(num))

if st.button("Generate Next Square"):
    try:
        st.write(f"Next square: `{next(squares_gen)}`")
    except StopIteration:
        st.error("No more squares to generate!")

# Section 4: Differences Between Iterators and Generators
st.markdown("## 🔹 Iterators vs. Generators")
differences = {
    "Feature": ["Memory Usage", "Complexity", "Implementation"],
    "Iterators": ["More memory-intensive", "Requires implementing `__iter__()` and `__next__()`", "Explicit class or function"],
    "Generators": ["Memory-efficient", "Simpler with `yield`", "Defined using functions"],
}
st.table(differences)

# Section 5: Use Cases for Generators
st.markdown("## 🔹 When to Use Generators?")
st.write("""
Generators are ideal for:
- Processing large datasets (e.g., reading large files).
- Infinite sequences (e.g., Fibonacci series).
- Pipelines that process data incrementally.
""")

# Interactive Example: Fibonacci Generator
st.markdown("### 🧪 Try It: Generate Fibonacci Numbers")
fib_limit = st.number_input("Enter the number of Fibonacci numbers to generate:", min_value=1, value=10)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib_gen = fibonacci(fib_limit)

if st.button("Generate Next Fibonacci Number"):
    try:
        st.write(f"Next Fibonacci number: `{next(fib_gen)}`")
    except StopIteration:
        st.error("No more Fibonacci numbers to generate!")

# Section 6: Best Practices and Pitfalls
st.markdown("## 🔹 Best Practices and Common Pitfalls")
st.write("""
- **Use Generators for Large Data**: They save memory by generating values on-the-fly.
- **Handle StopIteration**: Ensure your code can handle the end of iteration gracefully.
- **Avoid Reusing Generators**: Generators are exhausted after a single iteration.
""")

# Section 7: Quiz
st.markdown("## 🎮 Quiz: Test Your Knowledge!")
quiz_question = st.radio(
    "What is the difference between a function and a generator?",
    [
        "A function returns all values at once; a generator produces values one at a time using `yield`.",
        "A function is faster than a generator.",
        "Generators are not iterable."
    ]
)
if st.button("Submit Quiz Answer"):
    if quiz_question == "A function returns all values at once; a generator produces values one at a time using `yield`.":
        st.success("🎉 Correct! Generators produce values lazily, making them memory-efficient.")
    else:
        st.error("❌ Incorrect. Generators use `yield` to produce values lazily.")

# Section 8: Summary Table
st.markdown("## 📚 Summary")
summary_table = {
    "Feature": ["Iterators", "Generators"],
    "Definition": [
        "Objects that traverse collections using `__iter__()` and `__next__()`.",
        "Functions or expressions using `yield` to generate values lazily."
    ],
    "Use Case": [
        "Custom traversal logic, reusable for multiple iterations.",
        "Efficient memory usage, lazy evaluation, and pipelines."
    ]
}
st.table(summary_table)

# Footer
st.markdown("""
---
Made with ❤️ to help you master **Iterators and Generators in Python**.  
Keep exploring and building efficient code! 🚀
""")
