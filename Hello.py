import streamlit as st
from sklearn.datasets import load_sample_image

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to Culìculà! 👋")

    which_img = st.selectbox("Pick an image", options=["china.jpg", "flower.jpg"])
    img = load_sample_image(which_img)
    st.image(img)


if __name__ == "__main__":
    run()
