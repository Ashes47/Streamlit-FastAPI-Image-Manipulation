import io

import requests
from PIL import Image
from requests_toolbelt.multipart.encoder import MultipartEncoder

import streamlit as st

# interact with FastAPI endpoint
backend = "http://fastapi:8000/segmentation"


def process(image, timesUpscale, server_url: str):

    m = MultipartEncoder(fields={"file": ("filename", image, "image/jpeg")})

    r = requests.post(
        server_url, data=[m, timesUpscale], headers={"Content-Type": m.content_type}, timeout=8000
    )

    return r


st.sidebar.markdown("# Upscale Images")

st.title("Upscale Images")
st.write(
        """Stuff"""
    )  # description and instructions


# construct UI layout
st.title("Image Upscale")
st.write(
    """Stuff"""
)  # description and instructions

inputImage = st.file_uploader("Insert image")  # image upload widget

# Input 
timesUpscale = st.select_slider(
    "Upscale by:",
    options=["2", "4", "8"]
)

if st.button("Upscale"):

    col1, col2 = st.columns(2)

    if inputImage:
        segments = process(inputImage, timesUpscale, backend)
        original_image = Image.open(inputImage).convert("RGB")
        segmented_image = Image.open(io.BytesIO(segments.content)).convert("RGB")
        col1.header("Original")
        col1.image(original_image, use_column_width=True)
        col2.header("Segmented")
        col2.image(segmented_image, use_column_width=True)

    else:
        # handle case with no image
        st.write("Insert an image!")
