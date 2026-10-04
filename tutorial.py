import streamlit as st
import cv2
import numpy as np

st.title("Image Processing with OpenCV and Streamlit")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:

    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    # Convert bytes into OpenCV image
    image = cv2.imdecode(
        file_bytes,
        cv2.IMREAD_COLOR
    )

    # ORIGINAL IMAGE

    rgb_image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    st.image(
        rgb_image,
        caption="Original Image"
    )

    # GRAYSCALE IMAGE
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    st.image(
        gray,
        caption="Grayscale Image"
    )