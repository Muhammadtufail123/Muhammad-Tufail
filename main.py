import streamlit as st

def main():
    st.title("Simple Calculator")

    # Input fields for the two numbers
    num1 = st.number_input("Enter first number", value=0)
    num2 = st.number_input("Enter second number", value=0)

    # Dropdown for operation selection
    operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

    # Calculate result based on selected operation
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."

    # Display the result
    st.write(f"The result of {operation} is: {result}")

    # Show a confirmation prompt
    confirmation = st.selectbox("Do you want to continue with the calculator?", ("Yes", "No"))

    if confirmation == "No":
        st.markdown("The calculator is disabled. Please refresh the page if you want to continue with the browser.")
        # Disable inputs and dropdown
        st.markdown("<style>.stNumberInput, .stSelectbox {pointer-events: none;}</style>", unsafe_allow_html=True)

    # Footer message
    st.write("Application made by Muhammad Tufail")

if __name__ == "__main__":
    main()
