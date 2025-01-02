import streamlit as st

# Page Title
st.title("Welcome to Python Programming!")

# Brief Introduction
st.markdown("""
Python is one of the most popular and versatile programming languages today.  
It is known for its simplicity, readability, and a massive ecosystem of libraries and frameworks.  
Let's explore Python's journey and its amazing capabilities! 🚀
""")

# The History of Python
st.markdown("## 📜 The History of Python")
st.markdown("""
Python was created by **Guido van Rossum** in the late 1980s and released in **1991**.

- Guido wanted to design a language that prioritized **code readability** and allowed programmers to express concepts with fewer lines of code.
- The name **Python** doesn’t come from the snake! It was inspired by Guido’s love for the comedy series *Monty Python’s Flying Circus*.
""")

# Key Milestones
st.markdown("## 📅 Key Milestones in Python’s Evolution:")
st.markdown("""
1. **1991**: Python 1.0 was released with basic features like functions, modules, and exceptions.
2. **2000**: Python 2.0 introduced list comprehensions and garbage collection.
3. **2008**: Python 3.0 marked a major milestone with improvements but was **not backward-compatible**.
4. **2021**: Python 2 officially retired, solidifying Python 3 as the standard version.

**Fun Fact**: Python was named after a TV show, *Monty Python*, not the snake! ♻️
""")

# Why Learn Python
st.markdown("## 🤔 Why Learn Python?")
st.markdown("""
Python is widely used across industries, making it a great language to learn.  
Here are some reasons why Python is so popular:

- **Easy to Learn**: Its syntax is simple and beginner-friendly.
- **Versatile**: Python is used in web development, data analysis, AI and ML, automation, and more!
- **Extensive Libraries**: Libraries like NumPy, Pandas, TensorFlow, and Django make Python a powerhouse.
- **Strong Community**: Python has one of the largest and most supportive developer communities.
- **Great for Career Growth**: Many top companies, including Google, Netflix, and Spotify, use Python.
""")

# Interactive Section: Why Learn Python
st.markdown("## 🌟 Why do you want to learn Python?")
reason = st.radio(
    "Choose your reason:",
    ["Build web applications", "Analyze data", "Automate tasks", "Learn machine learning", "Just for fun!"]
)

if reason:
    st.write(f"Awesome! Learning Python for **'{reason}'** is a great choice! Let's get started. 🚀")

# What Can You Do with Python
st.markdown("## 🛠️ What Can You Do with Python?")
st.markdown("""
Python's versatility is unmatched. Here are some of its major applications:

1. **Web Development**:  
   Use frameworks like Django and Flask to build powerful web applications.
2. **Data Science and Visualization**:  
   Libraries like Pandas, NumPy, and Matplotlib make Python a favorite for data scientists.
3. **Artificial Intelligence (AI) and Machine Learning (ML)**:  
   Python powers AI/ML models using frameworks like TensorFlow and Scikit-learn.
4. **Automation and Scripting**:  
   Automate repetitive tasks with simple scripts.
5. **Game Development**:  
   Libraries like Pygame enable you to create games easily.
6. **Internet of Things (IoT)**:  
   Python integrates seamlessly with IoT devices for smart solutions.

""")
# Input for user excitement
user_interest = st.text_input("What excites you the most about Python? (e.g., AI, Web Development)")
if user_interest:
    st.write(f"That's fantastic! Python is perfect for exploring **{user_interest}**. 🎉")

# Python's Best Features
st.markdown("## ✨ Python's Best Features")
st.markdown("""
1. **Readable and Clean Syntax**:  
   Python code is easy to understand and write.  
   Example:
""")
st.code("""
# Python Code Example
for i in range(5):
    print("Python is awesome!")
""")
st.markdown("""
2. **Interpreted Language**:  
   Python doesn't need compilation, making it ideal for rapid development.
3. **Dynamic Typing**:  
   No need to declare variable types explicitly.
4. **Cross-Platform**:  
   Python works on Windows, Mac, and Linux.
5. **Extensive Libraries**:  
   Python has a library for almost everything, from web development to data analysis.
""")

# Quick Quiz
st.markdown("## 🎮 Quick Quiz: Test Your Knowledge")
quiz_answer = st.radio(
    "When was Python first released?",
    ["1991", "1989", "2000", "1995"]
)

if st.button("Submit Answer", key="quiz_button"):
    if quiz_answer == "1991":
        st.success("🎉 Correct! Python was first released in 1991.")
    else:
        st.error("❌ Incorrect. The correct answer is 1991.")

# Footer
st.markdown("""
---
Made with ❤️ to help you embark on your Python journey.  
**Happy Coding!** 🚀
""")
