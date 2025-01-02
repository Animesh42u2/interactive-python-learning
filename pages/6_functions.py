import streamlit as st
import pandas as pd

# Page Title
st.title("All About Python Functions 🛠️")

st.markdown("""
Functions in Python are reusable blocks of code that make your programs modular and efficient.  
They allow you to write clean, DRY (Don't Repeat Yourself) code! Let’s explore them in depth. 🚀  
""")

# Section 1: Defining Functions
st.markdown("## 🔹 Defining Functions")
st.write("""
In Python, a function is defined using the `def` keyword.  
Functions can take inputs (arguments), perform operations, and return results.
""")

st.markdown("### Syntax:")
st.code("""
def function_name(parameters):
    # Code block
    return value
""")

# Interactive Example: Define a Function
st.markdown("### 🧪 Try It: Define Your Own Function")

# Input widgets for function details
function_name = st.text_input("Name of your function:", "my_function")
argument_name = st.text_input("Name of the argument:", "name")
operation = st.text_area("Operation inside the function:", "return f'Hello, {name}!'")

# Button to run the function
if st.button("Run Your Function"):
    try:
        # Dynamically create the function using the input
        function_code = f"def {function_name}({argument_name}):\n    {operation}"
        
        # Use exec() to define the function dynamically in the local context
        exec(function_code)

        # Test the dynamically created function with a sample argument
        result = locals()[function_name]("Streamlit")  # Test with "Streamlit"

        # Display the result of the function
        st.write(f"Result of `{function_name}('Streamlit')`: {result}")

    except Exception as e:
        st.error(f"Error: {str(e)}")

# Section 2: Arguments and Return Values
st.markdown("## 🔹 Arguments and Return Values")
st.write("""
Functions can:
1. Take arguments as input.
2. Return values using the `return` keyword.
""")

st.markdown("### Example:")
st.code("""
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)  # Output: 8
""")

# Interactive Example: Add Two Numbers
st.markdown("### 🧪 Try It: Add Two Numbers")
num1 = st.number_input("Enter the first number:", value=0)
num2 = st.number_input("Enter the second number:", value=0)
if st.button("Add Numbers"):
    st.write(f"The sum of {num1} and {num2} is: {num1 + num2}")

# Section 3: Lambda Functions
st.markdown("## 🔹 Lambda Functions")
st.write("""
Lambda functions are anonymous functions defined with the `lambda` keyword.  
They are often used for small, single-line operations.
""")

st.markdown("### Example:")
st.code("""
# Lambda function to add two numbers
add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8
""")

# Interactive Example: Lambda Function
st.markdown("### 🧪 Try It: Create a Lambda Function")
lambda_expression = st.text_area("Write your lambda function:", "lambda x, y: x + y")
x_value = st.number_input("Enter the first value (x):", value=1)
y_value = st.number_input("Enter the second value (y):", value=2)
if st.button("Run Lambda Function"):
    try:
        result = eval(lambda_expression)(x_value, y_value)
        st.write(f"Result: `{result}`")
    except Exception as e:
        st.error(f"Error: {e}")

# Section 4: Recursion
st.markdown("## 🔹 Recursion")
st.write("""
A function can call itself, which is called recursion.  
Recursion is useful for problems like factorials, Fibonacci numbers, and traversing trees.
""")

st.markdown("### Example:")
st.code("""
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

result = factorial(5)
print(result)  # Output: 120
""")

# Interactive Example: Factorial Using Recursion
st.markdown("### 🧪 Try It: Calculate Factorial")
factorial_input = st.number_input("Enter a number:", min_value=0, value=5)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

if st.button("Calculate Factorial"):
    st.write(f"The factorial of {factorial_input} is: {factorial(factorial_input)}")

# Section 5: Default Arguments
st.markdown("## 🔹 Default Arguments")
st.write("""
Default arguments allow you to specify a default value for a parameter.  
If no value is provided during the function call, the default is used.
""")

st.markdown("### Example:")
st.code("""
def greet(name="World"):
    return f"Hello, {name}!"

print(greet())         # Output: Hello, World!
print(greet("Python")) # Output: Hello, Python!
""")

# Interactive Example: Default Arguments
st.markdown("### 🧪 Try It: Use Default Arguments")
default_name = st.text_input("Enter the default name:", "World")
custom_name = st.text_input("Enter a custom name (optional):", "")
if st.button("Greet"):
    def greet(name=default_name):
        return f"Hello, {name}!"
    st.write(greet(custom_name if custom_name else default_name))

# Section 6: Variable-length Arguments (*args and **kwargs)
st.markdown("## 🔹 Variable-length Arguments (`*args`, `**kwargs`)")
st.write("""
- **`*args`**: Allows a function to accept any number of positional arguments.
- **`**kwargs`**: Allows a function to accept any number of keyword arguments.
""")

st.markdown("### Example:")
st.code("""
def dynamic_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

dynamic_function(1, 2, 3, name="Python", version=3.9)
""")

# Interactive Example: Variable-length Arguments
st.markdown("### 🧪 Try It: Use `*args` and `**kwargs`")
args_input = st.text_input("Enter positional arguments (comma-separated):", "1, 2, 3")
kwargs_input = st.text_input("Enter keyword arguments (key=value, comma-separated):", "name=Python, version=3.9")

def dynamic_function(*args, **kwargs):
    st.write("Positional arguments:", args)
    st.write("Keyword arguments:", kwargs)

if st.button("Run `*args` and `**kwargs`"):
    args = tuple(map(str.strip, args_input.split(",")))
    kwargs = dict(pair.split("=") for pair in kwargs_input.split(","))
    dynamic_function(*args, **kwargs)

# Section 7: Summary Table
st.markdown("## 📚 Summary")
summary_table = pd.DataFrame({
    "Topic": [
        "Defining Functions", "Arguments and Return Values", 
        "Lambda Functions", "Recursion", 
        "Default Arguments", "*args and **kwargs"
    ],
    "Description": [
        "Create reusable code blocks using `def`.",
        "Functions can take inputs and return outputs.",
        "Anonymous one-liner functions using `lambda`.",
        "Functions that call themselves for repetitive tasks.",
        "Set default values for parameters in functions.",
        "Handle dynamic numbers of arguments and keyword arguments."
    ]
})
st.table(summary_table)

# Footer
st.markdown("""
---
Made with ❤️ to help you become a Python functions master!  
Keep learning and experimenting! 🚀
""")
