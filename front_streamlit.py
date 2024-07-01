import streamlit as st
import requests
from PIL import Image
import io
import subprocess
import time

# Iniciar el servidor FastAPI si no está en ejecución
def start_fastapi():
    try:
        # Intentará conectarse a la API
        response = requests.get("http://127.0.0.1:8000")
        if response.status_code == 200:
            st.write("El servidor de FastAPI está corriendo.")
    except requests.ConnectionError:
        # Si no se puede conectar, iniciar el servidor
        st.write("Starting FastAPI server...")
        subprocess.Popen(["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"])
        time.sleep(5)  # Espera a que el servidor inicie

start_fastapi()

st.title("Fire Detection App")

uploaded_file = st.file_uploader("Elige una imagen:", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # Save the uploaded file temporarily
    temp_path = "temp_uploaded_image.jpg"
    image.save(temp_path)
    
    # Display a progress spinner while the request is being processed
    with st.spinner('Detectando incendio...'):
        response = requests.post("http://127.0.0.1:8000/predict/", files={"file": open(temp_path, "rb")})
        
    if response.status_code == 200:
        result = response.json()
        is_fire = result.get('is_fire', None)
        if is_fire is not None:
            st.write(f"Prediccion: {'Incendio' if is_fire else 'No Incendio'}")
        else:
            st.write("Error: Unable to get a prediction.")
    else:
        st.write("Error: Unable to get a prediction.")

