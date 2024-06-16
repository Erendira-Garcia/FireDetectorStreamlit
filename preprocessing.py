# preprocessing.py
import cv2
import numpy as np

def preprocessing_image(filepath):
    img = cv2.imread(filepath)  # read

    if img is None:
        print(f"Error: Error al leer la imagen: {filepath}")
        return None

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    if img.shape[0] != 196 or img.shape[1] != 196:
        img = cv2.resize(img, (196, 196))

    img = img / 255
    return img
