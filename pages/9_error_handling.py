import streamlit as st

# Page Title
st.title("Error Handling⚠️")

st.markdown("""
Error handling is an essential part of programming.  
Python provides powerful tools like **try-except**, **raise**, and **custom exceptions** to gracefully handle errors in your code.  
Let’s dive in and explore error handling interactively! 🚀
""")

# Section 1: What is Error Handling?
st.markdown("## 🔹 What is Error Handling?")
st.write("""
Error handling refers to the process of anticipating, detecting, and responding to program errors.  
Python uses exceptions to handle errors. If an exception occurs, the program stops unless you catch and handle the error using **try-except** blocks.
""")

st.markdown("### Common Exceptions:")
st.table({
    "Exception": ["TypeError", "ValueError", "ZeroDivisionError", "FileNotFoundError"],
    "When It Occurs": [
        "When an operation or function is applied to an inappropriate type.",
        "When a function receives an argument of the right type but an inappropriate value.",
        "When dividing a number by zero.",
        "When trying to access a file that doesn’t exist.",
    ],
})

# Section 2: Try-Except Blocks
st.markdown("## 🔹 Using Try-Except Blocks")
st.write("""
The **try-except** block is used to handle exceptions. If an error occurs in the `try` block, the `except` block executes.  
You can also add an **else** block (executed if no error occurs) and a **finally** block (always executed).  
""")

st.markdown("### Syntax:")
st.code("""
try:
    # Code that might raise an exception
except ExceptionType:
    # Code to handle the exception
else:
    # Code to execute if no exception occurs
finally:
    # Code to execute regardless of an exception
""")

# Interactive Example: Division
st.markdown("### 🧪 Try It: Division with Error Handling")
numerator = st.number_input("Enter the numerator:", value=10)
denominator = st.number_input("Enter the denominator:", value=2)

try:
    result = numerator / denominator
    st.success(f"The result is {result}")
except ZeroDivisionError:
    st.error("❌ You cannot divide by zero!")
else:
    st.write("✅ Division was successful!")
finally:
    st.info("🔍 This block always runs.")

# Section 3: Raising Exceptions
st.markdown("## 🔹 Raising Exceptions")
st.write("""
Sometimes, you might want to raise an exception intentionally using the **`raise`** keyword.  
This is useful when you want to signal that something went wrong in your program.
""")

st.markdown("### Example:")
st.code("""
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    else:
        return "Valid age."

try:
    print(check_age(-5))
except ValueError as e:
    print(e)
""")

# Interactive Example: Raising an Exception
st.markdown("### 🧪 Try It: Check Your Age")
user_age = st.number_input("Enter your age:", value=18)

try:
    if user_age < 0:
        raise ValueError("Age cannot be negative!")
    st.success("✅ Your age is valid!")
except ValueError as e:
    st.error(f"❌ Error: {e}")

# Section 4: Custom Exceptions
st.markdown("## 🔹 Creating Custom Exceptions")
st.write("""
You can define your own exceptions by creating a class that inherits from Python’s built-in `Exception` class.  
Custom exceptions help make your code more meaningful and easier to debug.
""")

st.markdown("### Example:")
st.code("""
class CustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    raise CustomError("This is a custom error!")
except CustomError as e:
    print(e.message)
""")

# Interactive Example: Custom Exception
st.markdown("### 🧪 Try It: Custom Exception")
class CustomError(Exception):
    def __init__(self, message):
        self.message = message

try:
    st.button("Raise Custom Error", key="raise_error_button")
    raise CustomError("This is a custom exception triggered by the button!")
except CustomError as e:
    st.error(f"❌ Custom Error: {e.message}")

# Section 5: Best Practices
st.markdown("## 🔹 Best Practices for Error Handling")
st.write("""
- Catch specific exceptions rather than using a generic `except` block.
- Use `finally` to clean up resources like closing files or database connections.
- Avoid overusing exceptions for control flow.
- Provide meaningful error messages to help debug issues.
""")

# Section 6: Quiz
st.markdown("## 🎮 Quiz: Test Your Knowledge")
quiz_question = st.radio(
    "What will this code do?",
    options=[
        "Raise a TypeError",
        "Raise a ZeroDivisionError",
        "Raise a ValueError",
        "Nothing, it will run successfully"
    ],
)
st.code("""
try:
    x = int("Hello")
except ValueError:
    print("Invalid input!")
""")

if st.button("Submit Quiz Answer"):
    if quiz_question == "Raise a ValueError":
        st.success("🎉 Correct! Converting a non-numeric string to an integer raises a ValueError.")
    else:
        st.error("❌ Incorrect. The correct answer is: 'Raise a ValueError'.")

# Section 7: Summary
st.markdown("## 📚 Summary")
st.write("""
1. Use **try-except** to catch and handle exceptions.
2. Use **raise** to generate exceptions intentionally.
3. Create **custom exceptions** to handle specific error cases.
4. Always follow best practices for clean and effective error handling.
""")

# Footer
st.markdown("""
---
Made with ❤️ to help you master **Error Handling in Python**.  
Keep coding and debugging like a pro! 🚀  
""")
