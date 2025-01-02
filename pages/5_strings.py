import streamlit as st
import re
import textwrap

# Page Title
st.title("Strings🎉")
st.markdown("""
Strings are one of the most powerful and versatile data types in Python.  
This guide covers **everything about strings**, interactively! 🚀
""")

# Section 1: Basic String Operations
st.markdown("## 🔹 Basic String Operations")

# Creating Strings
st.markdown("### Creating Strings")
st.code("""
single_quote = 'Hello'
double_quote = "World"
triple_quote = '''Python
is
awesome!'''
""")

# Interactive Example: String Creation
string_input = st.text_input("Enter your string:", "Hello, Python!")
st.write(f"Your string: `{string_input}`")

# String Length
st.markdown("### String Length")
st.write(f"Length of your string: `{len(string_input)}`")

# Indexing and Slicing
st.markdown("### Indexing and Slicing")
st.write("Strings are zero-indexed, and you can use slicing for sub-strings.")
start_idx = st.number_input("Start Index:", min_value=0, max_value=len(string_input)-1, value=0)
end_idx = st.number_input("End Index:", min_value=start_idx, max_value=len(string_input), value=len(string_input))
st.write(f"Sliced String: `{string_input[start_idx:end_idx]}`")
st.write(f"Negative Indexing Example: Last character of the string: `{string_input[-1]}`")

# Section 2: String Methods
# User Input String
user_string = st.text_input("Enter a string to explore methods:", "Hello, Python!")

method = st.selectbox(
    "Choose a string method to apply:",
    [
        "lower", "upper", "capitalize", "title", "swapcase", 
        "strip", "lstrip", "rstrip", "replace", "split", 
        "join", "find", "count", "startswith", "endswith",
        "isalpha", "isdigit", "isspace", "isalnum"
    ]
)

# Method Handling
if method in ["lower", "upper", "capitalize", "title", "swapcase", "strip", "lstrip", "rstrip"]:
    # Methods that don't require additional parameters
    result = getattr(user_string, method)()
    st.write(f"Result of `{method}()`: `{result}`")

elif method == "replace":
    # Replace requires `old` and `new` strings
    old = st.text_input("Text to replace:", "Python")
    new = st.text_input("Replace with:", "Streamlit")
    if st.button("Apply Replace"):
        result = user_string.replace(old, new)
        st.write(f"Replaced String: `{result}`")

elif method == "split":
    # Split requires a delimiter
    delimiter = st.text_input("Delimiter for split (leave empty for whitespace):", "")
    if st.button("Apply Split"):
        result = user_string.split(delimiter or None)
        st.write(f"Split Result: `{result}`")

elif method == "join":
    # Join requires an iterable
    elements = st.text_area("Enter items to join (comma-separated):", "apple,banana,cherry")
    if st.button("Apply Join"):
        iterable = elements.split(",")
        result = user_string.join(iterable)
        st.write(f"Joined String: `{result}`")

elif method in ["find", "count", "startswith", "endswith"]:
    # Methods requiring substrings
    substring = st.text_input("Enter substring for the method:", "Python")
    if st.button(f"Apply `{method}`"):
        result = getattr(user_string, method)(substring)
        st.write(f"Result of `{method}('{substring}')`: `{result}`")

elif method in ["isalpha", "isdigit", "isspace", "isalnum"]:
    # Methods that return boolean values
    result = getattr(user_string, method)()
    st.write(f"Result of `{method}()`: `{result}`")


# Section 3: String Formatting
st.markdown("## 🔹 String Formatting")

# f-strings
name = st.text_input("Enter your name for formatting:", "Alice")
age = st.number_input("Enter your age:", min_value=0, value=30)
st.write(f"Formatted String (f-string): `Hello, {name}! You are {age} years old.`")

# Old-style formatting
st.write("Old-style Formatting: `Hello, %s! You are %d years old.`" % (name, age))

# Section 4: Escape Sequences
st.markdown("## 🔹 Escape Sequences")
st.code(r"""
new_line = "Line1\nLine2"
tab = "Column1\tColumn2"
backslash = "Backslash: \\"
raw_string = r"Raw string with \n no escape processing"
""")

# Section 5: Multiline Strings
st.markdown("## 🔹 Multiline Strings")
multiline_example = """This is
a multiline
string."""
st.code(multiline_example)

# Section 6: Concatenation and Repetition
st.markdown("## 🔹 Concatenation and Repetition")
concat_part1 = st.text_input("Enter first part:", "Hello")
concat_part2 = st.text_input("Enter second part:", "World")
repeat_count = st.slider("Repetition count:", 1, 10, 3)
st.write(f"Concatenated String: `{concat_part1 + ' ' + concat_part2}`")
st.write(f"Repeated String: `{concat_part1 * repeat_count}`")

# Section 7: Regular Expressions with Strings
st.markdown("## 🔹 Regular Expressions (Regex) with Strings")
regex_pattern = st.text_input("Enter a regex pattern:", r"\w+")
regex_matches = re.findall(regex_pattern, string_input)
st.write(f"Regex Matches: `{regex_matches}`")

# Section 8: String Comparisons
st.markdown("## 🔹 String Comparisons")
string2 = st.text_input("Enter another string for comparison:", "Hello, Streamlit!")
st.write(f"Are the strings equal? `{string_input == string2}`")
st.write(f"Lexicographical comparison: `{string_input} < {string2}: {string_input < string2}`")

# Section 9: Unicode and Encoding
st.markdown("## 🔹 Unicode and Encoding")
unicode_str = st.text_input("Enter a string to encode:", "Python 🐍")
encoded = unicode_str.encode("utf-8")
decoded = encoded.decode("utf-8")
st.write(f"Encoded String: `{encoded}`")
st.write(f"Decoded String: `{decoded}`")

# Section 10: Immutable Nature of Strings
st.markdown("## 🔹 Immutable Nature of Strings")
st.write("Strings are immutable. Modifications create a new string.")

# Section 11: Advanced String Techniques
st.markdown("## 🔹 Advanced String Techniques")
wrapped_text = textwrap.fill(string_input, width=30)
st.write("Text Wrapping Example:")
st.code(wrapped_text)

# Footer
st.markdown("""
---
Made with ❤️ to help you master Python Strings!  
Keep exploring and coding! 🚀
""")
