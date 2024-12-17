# Import Packages 

import pandas as pd
import streamlit as st
import sqlite3

# Database Connection
conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_userdata(username,password):
    c.execute('INSERT INTO userstable(username, password) VALUES (?,?)', (username, password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username=? AND password=?', (username, password))
    data = c.fetchall() 
    return data

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data


def main():
    """Simple Login App"""

    st.title("OreshBytes")

    menu = ["Home", "Login", "Signup"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Login":
        st.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')

        if st.sidebar.checkbox("Login"):

            # if password == '12345':
            create_usertable()
            result = login_user(username, password)
            
            if result:
                st.success("Logged In as {}".format(username))

                task = st.selectbox("Task", ["Add Post", "Analytics", "Profiles"])
                if task == "Add Post":
                    st.subheader("Add Your Post")

                elif task == "Analytics":
                    st.subheader("Analytics Section")

                elif task == "Profiles":
                    st.subheader("User Profiles")
                    user_result = view_all_users()
                    clean_df = pd.DataFrame(user_result, columns=["Username", "Password"])       
                    st.dataframe(clean_df)

            else:
                st.warning("Incorrect Username/Password")


    elif choice == "Signup":
        st.subheader("Signup Section")

        new_user = st.sidebar.text_input("Username")
        new_password = st.sidebar.text_input("Password", type='password')

        if st.sidebar.button("Signup"):
            create_usertable()
            add_userdata(new_user, new_password)



            st.sidebar.success("You have successfully created a valid Account")
            st.sidebar.info("Go to Login Menu to login")





if __name__ == '__main__':
    main()








