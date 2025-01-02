import streamlit as st
from abc import ABC, abstractmethod
import threading
import multiprocessing
import time

# Page Title
st.title("Explore Advanced Python Topics 🚀")
st.markdown("""
Python is a powerful language with advanced features that make it versatile and efficient.  
This guide will help you master advanced concepts interactively! 💡
""")

# Section 1: Context Managers and the `with` Statement
st.markdown("## 🔹 Context Managers and the `with` Statement")
st.write("""
Context managers handle resource management efficiently, such as opening files or database connections.  
The `with` statement ensures resources are cleaned up properly.
""")

st.markdown("### Example:")
st.code("""
with open("file.txt", "w") as f:
    f.write("Hello, World!")
# File is automatically closed after the block
""")

# Interactive Example: Write to a File
st.markdown("### 🧪 Try It: Write to a File Using `with`")
filename = st.text_input("Enter a filename:", "example.txt")
content = st.text_area("Enter content to write:", "Hello, Streamlit!")
if st.button("Write to File"):
    with open(filename, "w") as file:
        file.write(content)
    st.success(f"Content written to `{filename}`!")

# Section 2: Function Argument Unpacking (*args, **kwargs)
st.markdown("## 🔹 Function Argument Unpacking")
st.write("""
- **`*args`**: Allows a function to accept any number of positional arguments.
- **`**kwargs`**: Allows a function to accept any number of keyword arguments.
""")

st.markdown("### Example:")
st.code("""
def greet(*args, **kwargs):
    for name in args:
        print(f"Hello, {name}!")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet("Alice", "Bob", age=30, city="New York")
""")

# Interactive Example: Argument Unpacking
st.markdown("### 🧪 Try It: Use `*args` and `**kwargs`")
positional_args = st.text_input("Enter names (comma-separated):", "Alice, Bob")
keyword_args = st.text_input("Enter key-value pairs (e.g., age=30, city=NY):", "age=30, city=NY")

def greet(*args, **kwargs):
    greeting = [f"Hello, {name}!" for name in args]
    details = [f"{key}: {value}" for key, value in kwargs.items()]
    return greeting, details

if st.button("Run Function"):
    names = positional_args.split(", ")
    kwargs = dict(pair.split("=") for pair in keyword_args.split(", "))
    greetings, details = greet(*names, **kwargs)
    st.write("Greetings:", greetings)
    st.write("Details:", details)

# Section 3: Multiple Inheritance and MRO
st.markdown("## 🔹 Multiple Inheritance and MRO")
st.write("""
Multiple inheritance allows a class to inherit from multiple parent classes.  
Python uses the **Method Resolution Order (MRO)** to determine the order in which methods are resolved.
""")

st.markdown("### Example:")
st.code("""
class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    pass

c = C()
c.greet()  # Output: "Hello from A" (based on MRO)
""")

# Interactive Example: MRO
st.markdown("### 🧪 Try It: Understand MRO")
class A:
    def greet(self):
        return "Hello from A"

class B:
    def greet(self):
        return "Hello from B"

class C(A, B):
    pass

if st.button("Get MRO for Class C"):
    mro = C.mro()
    st.write("MRO:", [cls.__name__ for cls in mro])
    instance = C()
    st.write("C's `greet()` Output:", instance.greet())

# Section 4: Type Hinting
st.markdown("## 🔹 Type Hinting")
st.write("""
Type hinting improves code readability and helps tools like linters and IDEs catch type-related errors.
""")

st.markdown("### Example:")
st.code("""
def add(a: int, b: int) -> int:
    return a + b
""")

# Interactive Example: Use Type Hinting
st.markdown("### 🧪 Try It: Add Numbers with Type Hints")
num1 = st.number_input("Enter first number:", value=5)
num2 = st.number_input("Enter second number:", value=10)

def add(a: int, b: int) -> int:
    return a + b

if st.button("Add Numbers"):
    st.write(f"Sum: {add(num1, num2)}")

# Section 5: Abstract Base Classes (ABC)
st.markdown("## 🔹 Abstract Base Classes (ABC)")
st.write("""
Abstract base classes define a blueprint for derived classes, ensuring certain methods are implemented.
""")

st.markdown("### Example:")
st.code("""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
""")

# Interactive Example: ABC
st.markdown("### 🧪 Try It: Create an Abstract Class")
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return "Meow!"

cat = Cat()
st.write(f"Cat says: {cat.speak()}")

# Section 6: Multithreading and Multiprocessing
st.markdown("## 🔹 Multithreading and Multiprocessing")
st.write("""
- **Multithreading**: Runs multiple threads in the same process (limited by the GIL).
- **Multiprocessing**: Spawns separate processes to bypass the GIL for parallelism.
""")

st.markdown("### Example: Multithreading")
st.code("""
import threading

def task():
    print("Running task in thread")

thread = threading.Thread(target=task)
thread.start()
""")

# Interactive Example: Multiprocessing
st.markdown("### 🧪 Try It: Run a Multiprocessing Task")
st.code("""
import multiprocessing

def task():
    print("Running task in process")

process = multiprocessing.Process(target=task)
process.start()
""")
# Function to simulate a task
def process_task(output):
    output.put("Task running in a process!")
    time.sleep(2)
    output.put("Task completed!")
# Button and process management
if st.button("Start Multiprocessing"):
    output = multiprocessing.Queue()
    process = multiprocessing.Process(target=process_task, args=(output,))
    process.start()
    process.join()  # Ensure process finishes before proceeding
    while not output.empty():
        st.write(output.get())

# Footer
st.markdown("""
---
Made with ❤️ to help you master **Advanced Python Topics**.  
Keep learning and pushing your Python skills to the next level! 🚀
""")
