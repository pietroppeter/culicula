import streamlit as st
import numpy as np
from sklearn.datasets import load_sample_image

def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to :red[C]:gray[u]:green[l]:blue[ì] a color clustering app! 🎨")

    which_img = st.selectbox("Pick an image", options=["china.jpg", "flower.jpg"])
    img = load_sample_image(which_img)
    # st.write(img)
    # st.image(img)
    img_float = np.array(img, dtype=np.float64) / 255
    st.image(img_float) # works the same as img!


if __name__ == "__main__":
    run()
