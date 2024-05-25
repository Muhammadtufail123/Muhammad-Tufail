import streamlit as st

def main():
    st.title("Simple Calculator")

    # Input fields for the two numbers
    num1 = st.number_input("Enter first number", value=0.0, key='num1')
    num2 = st.number_input("Enter second number", value=0.0, key='num2')

    # Dropdown for operation selection
    operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

    # Initialize result variable
    result = None

    # Calculate result based on selected operation
    if operation and num1 is not None and num2 is not None:
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

        # Display the result if it's available
        st.write(f"The result of {operation} is: {result}")

        # Show a confirmation prompt if result is available
        confirmation = st.radio("Do you want to continue with the calculator?", ("Yes", "No"))

        if confirmation == "No":
            st.markdown("<style>.stNumberInput, .stSelectbox {pointer-events: none;}</style>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

