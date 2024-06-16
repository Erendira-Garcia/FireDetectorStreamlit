# main.py
from fastapi import FastAPI, UploadFile, File
from tensorflow.keras.models import load_model
import numpy as np
import cv2
from preprocessing import preprocessing_image
import uvicorn

app = FastAPI()

# Cargar el modelo
model = load_model('model.h5')

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image_path = "temp_image.jpg"

    with open(image_path, "wb") as f:
        f.write(contents)

    img = preprocessing_image(image_path)
    if img is None:
        return {"error": "Error al procesar la imagen"}

    img_array = np.expand_dims(img, axis=0)
    prediction = model.predict(img_array)
    is_fire = prediction[0][0] >= 0.5

    return {"is_fire": bool(is_fire)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)