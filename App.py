import streamlit as st
import pickle

st.set_page_config(
    page_title="My Profile",
    page_icon="👋",
)
# st.write("# Welcome to My Profile! 👋")
# st.sidebar.success("Select a demo above.")
st.title("Rizal Mujahiddan Profile")
st.header("About Me")
st.write(
    """
    A Person who interested Machine Learning, Data enthusiast, and Data science
    For Right now, I'm still learner about it.
    """
)

with st.container():
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("Education")
        st.markdown(
            """
            * IPB University 
            * SMAN 2 Depok
            """
        )
    with right_col:
        st.header("Project")
        st.markdown(
            """
            * Sklearn Bla Bla Bla 
            * Python Code Ilmiah
            """
        )
