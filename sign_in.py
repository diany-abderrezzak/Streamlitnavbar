import streamlit as st
from navbar import render_navbar

render_navbar()



def signin():
    st.title("Sign In")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign In"):
        # Add code here to validate user credentials from a database
        if email == "example@example.com" and password == "password":
            st.success("Sign in successful!")
            return True  # User signed in successfully
        else:
            st.error("Invalid email or password.")
    return False




if __name__ == "__main__":
    signin()


