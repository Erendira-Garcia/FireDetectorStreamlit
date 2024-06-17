from fastapi import FastAPI, UploadFile, File
from tensorflow.keras.models import load_model
import numpy as np
import cv2
from preprocessing import preprocessing_image
import uvicorn
import tempfile
import os

app = FastAPI()

# Cargar el modelo
model = load_model('model.h5')

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Crear un archivo temporal
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_image_file:
        temp_image_file.write(await file.read())
        temp_image_path = temp_image_file.name

    # Procesar la imagen
    img = preprocessing_image(temp_image_path)
    if img is None:
        os.remove(temp_image_path)
        return {"error": "Error al procesar la imagen"}

    img_array = np.expand_dims(img, axis=0)
    prediction = model.predict(img_array)
    is_fire = prediction[0][0] >= 0.5

    # Eliminar el archivo temporal
    os.remove(temp_image_path)

    return {"is_fire": bool(is_fire)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
