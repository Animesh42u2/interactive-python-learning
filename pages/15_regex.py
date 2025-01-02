import streamlit as st
import re

# Page Title
st.title("Master Regular Expressions in Python 🔍")
st.markdown("""
Regular expressions (regex) are powerful tools for searching and manipulating text.  
With Python's **`re` module**, you can use regex to solve complex text processing tasks efficiently. Let's dive in! 🚀
""")

# Section 1: Introduction to Regex
st.markdown("## 🔹 What Are Regular Expressions?")
st.write("""
Regular expressions are sequences of characters that define a search pattern.  
They are used for tasks like:
- Searching for patterns in text.
- Validating input (e.g., email addresses).
- Replacing text.
""")

st.markdown("### Example:")
st.code("""
# Example: Find all words in a string
import re
text = "Python is fun!"
words = re.findall(r"\\w+", text)
print(words)  # Output: ['Python', 'is', 'fun']
""")

# Section 2: Basic Patterns
st.markdown("## 🔹 Basic Patterns")
st.write("""
Here are some commonly used regex patterns:
- `.`: Matches any character except a newline.
- `\\d`: Matches any digit.
- `\\w`: Matches any word character (letters, digits, underscore).
- `\\s`: Matches any whitespace character.
- `*`: Matches 0 or more occurrences of the preceding element.
- `+`: Matches 1 or more occurrences of the preceding element.
- `?`: Matches 0 or 1 occurrence of the preceding element.
""")

# Interactive Example: Match Patterns
st.markdown("### 🧪 Try It: Match Patterns")
pattern = st.text_input("Enter a regex pattern:", r"\w+")
text_to_search = st.text_area("Enter text to search:", "Python is fun!")
matches = re.findall(pattern, text_to_search)
st.write(f"Matches: {matches}")

# Section 3: Searching, Matching, and Replacing
st.markdown("## 🔹 Searching, Matching, and Replacing")
st.write("""
The `re` module provides functions to work with regex:
- `re.search()`: Finds the first match of the pattern.
- `re.match()`: Matches the pattern at the start of the string.
- `re.findall()`: Finds all matches of the pattern.
- `re.sub()`: Replaces matches with a specified string.
""")

st.markdown("### Example:")
st.code("""
# Example: Replace digits with '*'
import re
text = "My phone number is 123-456-7890."
result = re.sub(r"\\d", "*", text)
print(result)  # Output: "My phone number is ***-***-****."
""")

# Interactive Example: Replace Text
st.markdown("### 🧪 Try It: Replace Matches")
replace_pattern = st.text_input("Enter a regex pattern to replace:", r"\d")
replacement_text = st.text_input("Enter replacement text:", "*")
text_to_replace = st.text_area("Enter text:", "My phone number is 123-456-7890.")
result = re.sub(replace_pattern, replacement_text, text_to_replace)
st.write(f"Replaced Text: {result}")

# Section 4: Grouping and Capturing
st.markdown("## 🔹 Grouping and Capturing")
st.write("""
Grouping allows you to create subpatterns and extract parts of matches:
- `( )`: Defines a group.
- `group(0)`: Returns the entire match.
- `group(n)`: Returns the nth group.
""")

st.markdown("### Example:")
st.code("""
# Example: Extract area code from a phone number
import re
text = "My phone number is (123) 456-7890."
match = re.search(r"\\((\\d{3})\\)", text)
if match:
    print(match.group(1))  # Output: "123"
""")

# Interactive Example: Extract Groups
st.markdown("### 🧪 Try It: Extract Groups")
group_pattern = st.text_input("Enter a regex pattern with groups:", r"\((\d{3})\)")
group_text = st.text_area("Enter text to extract groups from:", "My phone number is (123) 456-7890.")
group_match = re.search(group_pattern, group_text)
if group_match:
    st.write(f"Matched Group: {group_match.group(1)}")
else:
    st.write("No match found.")

# Section 5: Advanced Features
st.markdown("## 🔹 Advanced Features")
st.write("""
- **Lookahead and Lookbehind**: Assert that a string is (or isn’t) preceded or followed by another string.
  - `(?=...)`: Positive lookahead.
  - `(?!...)`: Negative lookahead.
  - `(?<=...)`: Positive lookbehind.
  - `(?<!...)`: Negative lookbehind.
- **Flags**: Modify regex behavior (e.g., `re.IGNORECASE`, `re.MULTILINE`).
""")

st.markdown("### Example:")
st.code("""
# Example: Case-insensitive matching
import re
text = "Python is FUN!"
match = re.search(r"fun", text, re.IGNORECASE)
print(bool(match))  # Output: True
""")

# Interactive Example: Case-Insensitive Matching
st.markdown("### 🧪 Try It: Case-Insensitive Search")
case_insensitive_pattern = st.text_input("Enter a regex pattern:", r"fun")
case_insensitive_text = st.text_area("Enter text:", "Python is FUN!")
case_match = re.search(case_insensitive_pattern, case_insensitive_text, re.IGNORECASE)
if case_match:
    st.write(f"Matched Text: {case_match.group(0)}")
else:
    st.write("No match found.")

# Section 6: Quiz
st.markdown("## 🎮 Quiz: Test Your Knowledge!")
quiz_question = st.radio(
    "What does the regex pattern `\\d+` match?",
    [
        "One or more digits",
        "Zero or more digits",
        "Any character except a digit",
        "Whitespace characters",
    ]
)
if st.button("Submit Quiz Answer"):
    if quiz_question == "One or more digits":
        st.success("🎉 Correct! `\\d+` matches one or more digits.")
    else:
        st.error("❌ Incorrect. The correct answer is: 'One or more digits'.")

# Section 7: Summary Table
st.markdown("## 📚 Summary")
summary_table = {
    "Pattern": [".", "\\d", "\\w", "\\s", "*", "+", "?"],
    "Description": [
        "Any character except newline",
        "Any digit (0-9)",
        "Any word character (letters, digits, underscore)",
        "Any whitespace character",
        "0 or more of the preceding element",
        "1 or more of the preceding element",
        "0 or 1 of the preceding element",
    ],
}
st.table(summary_table)

# Footer
st.markdown("""
---
Made with ❤️ to help you master **Regular Expressions in Python**.  
Keep exploring and building efficient text processing solutions! 🚀
""")
