import io
import requests
from PIL import Image
from requests_toolbelt.multipart.encoder import MultipartEncoder
import streamlit as st

# interact with FastAPI endpoint
upscaleAPI = "http://fastapi:8000/upscale"
statusAPI = "http://fastapi:8000/upscale/threads"

def process(image, modelUpscale):

    requestData = MultipartEncoder(fields={
        "modelUpscale": modelUpscale,
        "image": ("filename", image, "image/jpeg")
        })
    try:
        r = requests.post(
            upscaleAPI, data=requestData,  headers={"Content-Type": requestData.content_type}, timeout=30000
        )
        return r
    except Exception as e:
        st.error(e)

st.sidebar.markdown("# Upscale Images")

st.title("Upscale Images")
st.write(
        """Upscale image using RealESRGAN"""
    )  # description and instructions


# construct UI layout
st.title("Image Upscale")
st.write(
    """Upload the image and choose upscalling percentage"""
)  # description and instructions

inputImage = st.file_uploader("Insert image")  # image upload widget

# Input 
modelUpscale = st.select_slider(
    "Upscale by:",
    options=["2", "4", "8"]
)

if st.button("Upscale"):
    col1, col2 = st.columns(2)
    if inputImage:
        upscaleResponse = process(inputImage, modelUpscale)
        originalImage = Image.open(inputImage).convert("RGB")
        upscaledImage = Image.open(io.BytesIO(upscaleResponse.content)).convert("RGB")
        col1.header("Original")
        col1.image(originalImage, use_column_width=True)
        col2.header("Upscaled Image")
        col2.image(upscaledImage, use_column_width=True)
    else:
        # handle case with no image
        st.write("Insert an image!")

if st.button('Check Status'):
    try:
        data = requests.get(statusAPI).json()
        st.write(f"Threads Running: {data['threads_running']}")
    except Exception as e:
        st.error(e)