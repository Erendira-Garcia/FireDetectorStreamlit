# FireDetector

## API del proyecto Detector de incendios del programa "Mil mujeres en IA" 2024

Para ejecutar la API:

	- Crear el entorno virtual: 
  	python -m venv env (env es el nombre del entorno en este caso)

	- Activar el entorno virtual:
  	Windows: env\Scripts\activate
  	macOS/Linux: source env/bin/activate

	- Instalar las dependencias: 
  	pip install -r requirements.txt

	- Ejecutar: 
  	uvicorn main:app --reload

Para probar la API:

  En Postman:

	- Abrir Postman y selecciona el método POST

	- Introducir la URL: http://localhost:8000/predict

	- En la pestaña Body, seleccionar form-data

	- Escribe file en el campo Key y selecciona el tipo File

	- Sube una imagen en el campo de Value (New file from local machine)

	- Presiona Send para relaizar la solicitud 

  En FastAPI:

	- Abre http://localhost:8000/docs

	- Busca el endpoint POST/predict/

	- Haz clic en el botón Try it out

	- Sube una imagen en el campo de archivo

	- Haz clic en el botón Execute para enviar la solicitud



