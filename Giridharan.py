import streamlit as st
st.title("Student Portfolio")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Skills", "Projects", "Contact"])
if page == "Home":
    st.header("Welcome to My Portfolio!")
    st.write("Hello! I'm a college student pursuing a degree in Engineering. "
             "This is my personal portfolio showcasing my skills, projects, and contact information.")
elif page == "About Me":
    st.header("About Me")
    st.write(''''Hello i am giridharan iam currently pursuving my under graduation in Artificial inteligence and data science
,my hobbies are playing keyboard which help me to think in different way ''')
elif page == "Skills":
    st.header("Skills")
    st.write("Here are some of my skills:")
    st.write("- Programming Languages: Python")
    st.write("- Other: Problem-solving, Hardwork,Dedication")
elif page == "Projects":
    st.header("Projects")
    st.write("Here are some of my recent projects:")
    st.write("1. Portfolio Website - A personal portfolio website created with Streamlit.")

elif page == "Contact":
    st.header("Contact Me")
    st.write("moble no-9025328986")
    st.write("Email:giridharan15062006jehova@gmail.com")
             