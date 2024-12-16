import streamlit as st

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

            if password == '12345':
                st.success("Logged In as {}".format(username))

                task = st.selectbox("Task", ["Add Post", "Analytics", "Profiles"])
                if task == "Add Post":
                    st.subheader("Add Your Post")

                elif task == "Analytics":
                    st.subheader("Analytics Section")

                elif task == "Profiles":
                    st.subheader("User Profiles")

            else:
                st.warning("Incorrect Username/Password")

    elif choice == "Signup":
        st.subheader("Signup Section")

        new_user = st.sidebar.text_input("Username")
        new_password = st.sidebar.text_input("Password", type='password')

        if st.sidebar.button("Signup"):
            st.sidebar.success("You have successfully created a valid Account")
            st.sidebar.info("Go to Login Menu to login")





if __name__ == '__main__':
    main()








