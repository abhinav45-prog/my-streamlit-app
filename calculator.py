import streamlit as st

# Title
st.title("Simple Calculator")

# Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Inputs
a = st.number_input("Enter first number", step=1.0)
b = st.number_input("Enter second number", step=1.0)

# Operation selection
choice = st.selectbox(
    "Choose operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Button
if st.button("Calculate"):
    if choice == "Addition":
        result = add(a, b)
    elif choice == "Subtraction":
        result = subtract(a, b)
    elif choice == "Multiplication":
        result = multiply(a, b)
    elif choice == "Division":
        result = divide(a, b)

    st.success(f"Result: {result}")
    
import streamlit as st

st.title("Welcome to the BMI Calculator App!")
st.write("This is a simple BMI calculator.")

weight = st.text_input("Enter your weight in kg:")
height = st.text_input("Enter your height in m:")

if st.button("Calculate BMI"):
    if weight and height:
        weight = float(weight)
        height = float(height)
        bmi = weight / (height ** 2)

        st.success(f"Your BMI is: {bmi:.3f}")

        if bmi < 18.5:
            st.warning("You are underweight.")
        elif bmi < 25:
            st.success("You have a normal weight.")
        elif bmi < 30:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")

