import io
from starlette.responses import Response
from fastapi import FastAPI, File, Form
import threading
from upscale import load_models, upscale, get_device

app = FastAPI(
    title="Upscale Images",
    description="""Upscale images using RealESRGAN""",
    version="0.1.0",
)

@app.get("/upscale/threads")
async def get_threads_running():
    return {
        "threads_running": threading.active_count(),
        "device": get_device()
        }


@app.post("/upscale")
async def get_upscale_image(image: bytes = File(default=None), modelUpscale: int = Form(default=None)):
    """Get upscale iamge from image file"""
    if image or modelUpscale:
        upscaledImage = await upscale_image(image, modelUpscale)
        bytes_io = io.BytesIO()
        upscaledImage.save(bytes_io, format="PNG")
        return Response(bytes_io.getvalue(), media_type="image/png")
    else:
        return {"Error:": "Data Invalid!"}

async def upscale_image(image, modelUpscale):
    model = load_models(modelUpscale)
    return upscale(model, image)
