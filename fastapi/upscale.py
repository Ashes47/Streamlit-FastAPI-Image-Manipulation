import io
from PIL import Image
if not hasattr(Image, 'Resampling'):  # Pillow<9.0
    Image.Resampling = Image
import numpy as np
import torch
from RealESRGAN import RealESRGAN

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def get_device():
    if torch.cuda.is_available():
        return 'cuda'
    return 'cpu'
    
def load_models(model_scale):
    if model_scale == 2:
        model_2 = RealESRGAN(device, scale = model_scale)
        model_2.load_weights(f'weights/RealESRGAN_x2.pth')  # GPU 1982 MB   Base 804 MB
        return model_2
    if model_scale == 4:
        model_4 = RealESRGAN(device, scale = model_scale)
        model_4.load_weights(f'weights/RealESRGAN_x4.pth')  # GPU 2284 MB   Base 804 MB
        return model_4
    if model_scale == 8:
        model_8 = RealESRGAN(device, scale = model_scale)
        model_8.load_weights(f'weights/RealESRGAN_x8.pth')  # GPU 6482 MB   Base 804 MB
        return model_8

def upscale(model, image):
    # Predicting
    input_image = Image.open(io.BytesIO(image)).convert("RGB")
    with torch.no_grad():
        upscaledImage = model.predict(lr_image = np.array(input_image))
    if device == 'cuda':
        torch.cuda.empty_cache()
    return upscaledImage
