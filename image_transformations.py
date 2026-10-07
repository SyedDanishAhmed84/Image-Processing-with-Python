import streamlit as st
import cv2
import numpy as np

st.title("Image Processing with OpenCV and Streamlit")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "png", "jpeg"]
)

if uploaded_file is not None:

    # Read uploaded file
    file_bytes = np.asarray(
        bytearray(uploaded_file.read()),
        dtype=np.uint8
    )

    image = cv2.imdecode(
        file_bytes,
        cv2.IMREAD_COLOR
    )

    # Convert BGR → RGB
    rgb_image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    st.subheader("Original Image")
    st.image(rgb_image)

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    st.subheader("Grayscale")
    st.image(gray)

    # -------------------------
    # RESIZE
    # -------------------------

    resized = cv2.resize(
        image,
        (400, 300)
    )

    resized_rgb = cv2.cvtColor(
        resized,
        cv2.COLOR_BGR2RGB
    )

    st.subheader("Resized Image")
    st.image(resized_rgb)

    cropped = image[50:300, 100:400]

    cropped_rgb = cv2.cvtColor(
        cropped,
        cv2.COLOR_BGR2RGB
    )

    st.subheader("Cropped Image")
    st.image(cropped_rgb)

    rotated = cv2.rotate(
        image,
        cv2.ROTATE_90_CLOCKWISE
    )

    rotated_rgb = cv2.cvtColor(
        rotated,
        cv2.COLOR_BGR2RGB
    )

    st.subheader("Rotated Image")
    st.image(rotated_rgb)


    flipped = cv2.flip(
        image,
        1
    )

    flipped_rgb = cv2.cvtColor(
        flipped,
        cv2.COLOR_BGR2RGB
    )

    st.subheader("Flipped Image")
    st.image(flipped_rgb)