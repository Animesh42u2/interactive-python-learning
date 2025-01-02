import streamlit as st
import os
from pathlib import Path
from datetime import datetime

# Page Title
st.title("Mastering File Handling in Python 📝")

st.markdown("""
File handling is an essential part of Python programming. It allows you to read, write, and manage files effectively.  
Let’s explore **file handling** concepts in detail with interactive examples and fun tasks! 🚀  
""")

# Section 1: Basics of File Handling
st.markdown("## 🔹 Basics of File Handling")
st.write("""
File handling in Python is done using built-in functions like `open()`, `read()`, `write()`, and `close()`.  
Python provides easy ways to work with files using different file modes:
- **`r`**: Read-only mode
- **`w`**: Write-only mode (overwrites existing content)
- **`a`**: Append mode (adds new content to the file)
- **`r+`**: Read and write mode
""")

# Section 2: Reading Files
st.markdown("## 🔹 Reading Files")
st.write("""
Reading a file is one of the most common tasks. Let's see the functions used for reading:
- **`read()`**: Reads the entire file content.
- **`readline()`**: Reads a single line from the file.
- **`readlines()`**: Reads all lines and returns them as a list.
""")

# Interactive Example: Reading a File
st.markdown("### 🧪 Try It: Read a File")
file_to_read = st.file_uploader("Upload a text file to read", type=["txt"])
if file_to_read is not None:
    file_content = file_to_read.read().decode("utf-8")
    st.text_area("File Content:", file_content, height=200)

    st.markdown("#### Read Methods:")
    st.write(f"File size: `{len(file_content)} bytes`")
    st.write(f"First line: `{file_content.splitlines()[0]}` (using `readline()`)")

# Section 3: Writing to Files
st.markdown("## 🔹 Writing to Files")
st.write("""
Writing to files is done using:
- **`write()`**: Writes a single string to the file.
- **`writelines()`**: Writes a list of strings to the file.
""")

# Interactive Example: Writing to a File
st.markdown("### 🧪 Try It: Write to a File")
user_text = st.text_area("Write something to a file:")
if st.button("Save to File"):
    with open("user_file.txt", "w") as f:
        f.write(user_text)
    st.success("Your text has been saved to `user_file.txt`!")

# Section 4: File Modes
st.markdown("## 🔹 File Modes")
file_modes = {
    "r": "Read (default). Opens the file for reading.",
    "w": "Write. Creates a new file or overwrites an existing file.",
    "a": "Append. Adds new content to the file without overwriting.",
    "r+": "Read and Write. Opens the file for both operations.",
}
st.table(file_modes)

# Section 5: Context Managers (`with` Statement)
st.markdown("## 🔹 Context Managers (`with` Statement)")
st.write("""
Using the **`with`** statement ensures that the file is properly closed after the operation.  
This is considered the best practice for file handling.
""")

st.markdown("### Example:")
st.code("""
with open("example.txt", "r") as f:
    content = f.read()
print(content)  # File is automatically closed after the block
""")

# Section 6: Working with Directories
st.markdown("## 🔹 Working with Directories")
st.write("""
Python provides modules like `os` and `pathlib` to work with directories.  
You can create, delete, and list files and directories easily.
""")

# Subsection: List Files in a Directory
st.markdown("### 📂 List Files in a Directory")
dir_path = st.text_input("Enter a directory path to list files:", value=str(Path.cwd()))
if os.path.isdir(dir_path):
    files = os.listdir(dir_path)
    st.write(f"Files in `{dir_path}`:")
    st.write(files)
else:
    st.error("Invalid directory path!")

# Subsection: Create and Delete Files
st.markdown("### 🛠️ Create and Delete Files")
file_name = st.text_input("Enter a file name to create:", value="new_file.txt")
if st.button("Create File"):
    with open(file_name, "w") as f:
        f.write("This is a new file created using Python.")
    st.success(f"File `{file_name}` created successfully!")
if st.button("Delete File"):
    if os.path.exists(file_name):
        os.remove(file_name)
        st.success(f"File `{file_name}` deleted successfully!")
    else:
        st.error("File does not exist!")

# Subsection: Using `pathlib`
st.markdown("### 🛠️ Using `pathlib`")
st.write("`pathlib` is an object-oriented module for working with file paths.")
st.code("""
from pathlib import Path

path = Path("example.txt")
print(path.exists())  # Check if the file exists
""")
example_path = Path("example.txt")
st.write(f"Does `example.txt` exist? `{example_path.exists()}`")

# Section 7: Working with Timestamps
st.markdown("## 🔹 File Timestamps")
st.write("Use the `datetime` module to work with file timestamps.")
st.code("""
from datetime import datetime
import os

file_time = os.path.getmtime("example.txt")
print(datetime.fromtimestamp(file_time))
""")
if example_path.exists():
    timestamp = datetime.fromtimestamp(example_path.stat().st_mtime)
    st.write(f"Last modified time of `example.txt`: `{timestamp}`")

# Section 8: Quiz
st.markdown("## 🎮 Quiz: Test Your Knowledge")
quiz_question = st.radio(
    "What does the following code do?",
    options=[
        "Reads all lines of the file as a list.",
        "Writes a list of strings to the file.",
        "Reads the first line of the file."
    ]
)
st.code("""
with open("example.txt", "r") as f:
    lines = f.readlines()
""")

if st.button("Submit Quiz Answer"):
    if quiz_question == "Reads all lines of the file as a list.":
        st.success("🎉 Correct! `readlines()` reads all lines of the file into a list.")
    else:
        st.error("❌ Incorrect. The correct answer is: 'Reads all lines of the file as a list.'")

# Section 9: Summary
st.markdown("## 📚 Summary")
st.write("""
1. **Reading Files**: Use `read()`, `readline()`, or `readlines()` to read file content.
2. **Writing Files**: Use `write()` or `writelines()` to write to files.
3. **File Modes**: Choose the appropriate mode (`r`, `w`, `a`, etc.) based on your task.
4. **Context Managers**: Use the `with` statement for safe and clean file handling.
5. **Working with Directories**: Use `os` or `pathlib` to interact with directories and files.
""")

# Footer
st.markdown("""
---
Made with ❤️ to help you master **File Handling in Python**.  
Happy File Management! 🚀  
""")
