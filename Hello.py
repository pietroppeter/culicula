import streamlit as st
from sklearn.datasets import load_sample_image

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Culìculà! 👋")

    img = load_sample_image("china.jpg")
    st.image(img)




if __name__ == "__main__":
    run()
