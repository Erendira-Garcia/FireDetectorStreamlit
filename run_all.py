import subprocess
import threading

# Función para ejecutar FastAPI
def run_fastapi():
    subprocess.run(["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"])

# Función para ejecutar Streamlit
def run_streamlit():
    subprocess.run(["streamlit", "run", "front_streamlit.py"])

# Crear hilos para ejecutar ambos servicios en paralelo
fastapi_thread = threading.Thread(target=run_fastapi)
streamlit_thread = threading.Thread(target=run_streamlit)

# Iniciar ambos hilos
fastapi_thread.start()
streamlit_thread.start()

# Esperar a que ambos hilos terminen
fastapi_thread.join()
streamlit_thread.join()

