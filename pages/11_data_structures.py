import streamlit as st

# Page Title
st.title("Python Data Structures 🗃️")
st.markdown("""
Data structures are essential for organizing and managing data efficiently. Python offers a variety of built-in and advanced data structures to solve problems effectively. Let's dive in! 🚀
""")

# Section 1: Lists
st.markdown("## 🔹 Lists")
st.write("""
Lists are mutable, ordered collections that can hold elements of any type.  
They are ideal for storing data that you need to modify or iterate over.
""")

st.code("""
# List Example
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add an element
print(fruits[1])         # Access by index
""")

# Interactive Example: Lists
st.markdown("### 🧪 Try It: Manage Your Shopping List")
shopping_list = st.text_area("Enter items for your shopping list (comma-separated):", "milk, eggs, bread")
shopping_list = shopping_list.split(", ")
shopping_list_action = st.radio("What would you like to do?", ["View List", "Add Item", "Remove Item"])
if shopping_list_action == "Add Item":
    new_item = st.text_input("Enter item to add:")
    if new_item:
        shopping_list.append(new_item)
        st.success(f"Added {new_item} to the list!")
elif shopping_list_action == "Remove Item":
    remove_item = st.selectbox("Select item to remove:", shopping_list)
    shopping_list.remove(remove_item)
    st.success(f"Removed {remove_item} from the list!")
st.write("Your Shopping List:", shopping_list)

# Section 2: Tuples
st.markdown("## 🔹 Tuples")
st.write("""
Tuples are immutable, ordered collections.  
They are useful for fixed data, like coordinates or configuration settings.
""")
st.code("""
# Tuple Example
coordinates = (10, 20)
print(coordinates[0])  # Access by index
""")

# Interactive Example: Tuples
st.markdown("### 🧪 Try It: Create a Tuple of Coordinates")
x_coord = st.number_input("Enter x-coordinate:", value=0)
y_coord = st.number_input("Enter y-coordinate:", value=0)
coordinates = (x_coord, y_coord)
st.write(f"Your Coordinates: {coordinates}")

# Section 3: Dictionaries
st.markdown("## 🔹 Dictionaries")
st.write("""
Dictionaries store data in key-value pairs.  
They are perfect for representing mappings, like a phonebook or JSON data.
""")
st.code("""
# Dictionary Example
phonebook = {"Alice": "123-456", "Bob": "987-654"}
print(phonebook["Alice"])  # Access by key
""")

# Interactive Example: Dictionaries
st.markdown("### 🧪 Try It: Manage a Phonebook")
phonebook = {}
name = st.text_input("Enter name:")
number = st.text_input("Enter phone number:")
if st.button("Add to Phonebook"):
    phonebook[name] = number
    st.success(f"Added {name}: {number}")
st.write("Phonebook:", phonebook)

# Section 4: Sets
st.markdown("## 🔹 Sets")
st.write("""
Sets are unordered collections of unique elements.  
They are great for removing duplicates and performing mathematical operations like unions and intersections.
""")
st.code("""
# Set Example
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Union
print(a & b)  # Intersection
""")

# Interactive Example: Sets
st.markdown("### 🧪 Try It: Perform Set Operations")
set1 = set(st.text_input("Enter elements of Set 1 (comma-separated):", "1, 2, 3").split(", "))
set2 = set(st.text_input("Enter elements of Set 2 (comma-separated):", "3, 4, 5").split(", "))
operation = st.radio("Choose an operation:", ["Union", "Intersection", "Difference"])
if operation == "Union":
    result = set1 | set2
elif operation == "Intersection":
    result = set1 & set2
elif operation == "Difference":
    result = set1 - set2
st.write("Result:", result)

# Section 5: Stacks and Queues
st.markdown("## 🔹 Stacks and Queues")
st.write("""
- **Stacks**: Follow the Last In First Out (LIFO) principle.
- **Queues**: Follow the First In First Out (FIFO) principle.
""")
st.code("""
# Stack Example
stack = []
stack.append(10)  # Push
stack.pop()       # Pop

# Queue Example
from collections import deque
queue = deque()
queue.append(10)  # Enqueue
queue.popleft()   # Dequeue
""")

# Interactive Example: Stacks
st.markdown("### 🧪 Try It: Use a Stack")
stack = []
stack_action = st.radio("Choose a Stack Action:", ["Push", "Pop", "View"])
if stack_action == "Push":
    push_value = st.number_input("Enter value to push:", value=0)
    stack.append(push_value)
    st.success(f"Pushed {push_value} onto the stack!")
elif stack_action == "Pop":
    if stack:
        popped_value = stack.pop()
        st.success(f"Popped {popped_value} from the stack!")
    else:
        st.error("Stack is empty!")
st.write("Current Stack:", stack)

# Section 6: Trees
st.markdown("## 🔹 Trees")
st.write("""
Trees are hierarchical data structures with nodes.  
Each node has a value and children, except for the root node, which has no parent.
""")
st.code("""
# Binary Tree Example
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
print(root.left.value)  # Output: 2
""")

# Section 7: Graphs
st.markdown("## 🔹 Graphs")
st.write("""
Graphs are a collection of nodes connected by edges.  
They are widely used in networks, social media, and route optimization.
""")
st.code("""
# Graph Example
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C"]
}
print(graph["A"])  # Output: ['B', 'C']
""")

# Interactive Example: Create a Graph
st.markdown("### 🧪 Try It: Create a Graph")
node = st.text_input("Enter node name:")
connected_nodes = st.text_area("Enter connected nodes (comma-separated):", "B, C")
graph = {}
if node and connected_nodes:
    graph[node] = connected_nodes.split(", ")
    st.write("Graph:", graph)

# Footer
st.markdown("""
---
Made with ❤️ to help you master **Data Structures** in Python.  
Keep coding and exploring! 🚀
""")
