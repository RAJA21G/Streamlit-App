# -*- coding: utf-8 -*-
"""Calculator App .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Qd8Ix_A5BraT93Mfsd9ZMjovP_FlOKiy
"""

import streamlit as st

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Streamlit App UI
def calculator_app():
    st.title("Simple Calculator")

    # Select operation
    operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])

    # Input numbers
    num1 = st.number_input("Enter first number", format="%.2f")
    num2 = st.number_input("Enter second number", format="%.2f")

    # Perform calculation based on operation
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    # Display the result
    if st.button("Calculate"):
        st.write(f"Result: {result}")

# Run the Streamlit app
if __name__ == "__main__":
    calculator_app()