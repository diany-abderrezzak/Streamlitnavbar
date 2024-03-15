import streamlit as st

def render_navbar():
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    st.markdown(
        """
        <style>
        ul {
            width: 100%;
            position: fixed;
            top: 0;
            left: 0;
            list-style-type: none;
            margin: 0;
            padding: 0;
            overflow: hidden;
            background-color: #333;
        }

        li {
            float: left;
        }

        li a {
            display: block;
            color: #f2f2f2;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
        }

        li a:hover:not(.active) {
            background-color: #111;
            border-radius:10px;
        }

        .active {
            background-color: #04AA6D;
        }
        .navbar a {
            display: block;
            color: #f2f2f2;
            text-align: center;
            padding: 14px 20px;
            text-decoration: none;
            font-size: 17px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
            <ul class="navbar">
              <li><a href=" http://localhost:8501" target="_parent">Home</a></li>
              <li><a href="#news">News</a></li>
              <li><a href="#contact">Contact</a></li>
              <li style="float:right"><a class="active" target="_parent" href="http://localhost:8502">sign up</a></li>
              <li style="float:right"><a class="active" target="_parent" href="http://localhost:8503">Login</a></li>
            </ul>
            """,
        unsafe_allow_html=True
    )
