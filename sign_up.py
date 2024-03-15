import streamlit as st
from navbar import render_navbar

render_navbar()

def student_registration():
    st.title("Student Registration Form")

    # Input fields
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=150, step=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    course = st.text_input("Course")
    address = st.text_area("Address")
    email = st.text_input("Email")

    if st.button("Submit"):

        if name and age and gender and course and address and email:

            st.success("Registration successful!")
        else:
            st.error("Please fill in all fields.")

def main():
    student_registration()

if __name__ == "__main__":
    main()

