from time import time

import streamlit as st

import numpy as np

from sklearn.datasets import load_sample_image
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from sklearn.metrics import pairwise_distances_argmin


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

    # Convert to floats instead of the default 8 bits integer coding. Dividing by
    # 255 is important so that plt.imshow behaves works well on float data (need to
    # be in the range [0-1])
    img_float = np.array(img, dtype=np.float64) / 255
    st.image(img_float) # works the same as img!

    # Load Image and transform to a 2D numpy array.
    w, h, d = original_shape = tuple(img_float.shape)
    assert d == 3
    img_array = np.reshape(img_float, (w * h, d))

    n_colors = st.number_input("How many colors?", min_value=2, max_value=256, value=8)

    st.write("Fitting model on a small sub-sample of the data")
    t0 = time()
    img_array_sample = shuffle(img_array, random_state=0, n_samples=1_000)
    kmeans = KMeans(n_clusters=n_colors, n_init="auto", random_state=0).fit(
        img_array_sample
    )
    st.write(f"done in {time() - t0:0.3f}s.")

    # Get labels for all points
    st.write("Predicting color indices on the full image (k-means)")
    t0 = time()
    labels = kmeans.predict(img_array)
    st.write(f"done in {time() - t0:0.3f}s.")

    st.write(f"### Quantized image ({n_colors} colors, K-Means)")
    st.image(recreate_image(kmeans.cluster_centers_, labels, w, h))

    # random color selection
    codebook_random = shuffle(img_array, random_state=0, n_samples=n_colors)
    st.write("Predicting color indices on the full image (random)")
    t0 = time()
    labels_random = pairwise_distances_argmin(codebook_random, img_array, axis=0)
    st.write(f"done in {time() - t0:0.3f}s.")

    st.write(f"### Quantized image ({n_colors} colors, Random)")
    st.image(recreate_image(codebook_random, labels_random, w, h))


def recreate_image(codebook, labels, w, h):
    """Recreate the (compressed) image from the code book & labels"""
    return codebook[labels].reshape(w, h, -1)

if __name__ == "__main__":
    run()
