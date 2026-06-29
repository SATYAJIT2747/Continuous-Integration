import streamlit as st
st.title("Power Calculator App")
st.write("Enter a number to calculate its square, cube, and fifth power.")
number = st.number_input("Enter a number:", value=0.0)

# Calculate powers
square = number ** 2
cube = number ** 3
fifth_power = number ** 5

# Display results
st.write(f"the square of {number} is: {square}")
st.write(f"the cube of {number} is: {cube}")
st.write(f"the fifth power of {number} is: {fifth_power}")