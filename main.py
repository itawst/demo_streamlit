import streamlit as st 
st.title("This is my first web app using stramlit")

def my_program():
    name = "Hello World !!"
    print("this is new code")
    return name

result = my_program()
st.write(result)