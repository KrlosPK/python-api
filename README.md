# Python API using FastAPI

## Descripción

Esta es una API para gestionar dragones, jinetes y aliados en un mundo ficticio, construida con FastAPI y Python. Provee endpoints para crear, leer, actualizar y eliminar información de dragones, jinetes y aliados.

## Requisitos

- Python 3.8+
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn (para correr el servidor)

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/KrlosPK/python-api
   cd python-api
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python -m venv modules
   cd modules
   cd Scripts
   activate
   ```

3. Instala las dependencias (En la ruta raíz del proyecto):

   ```bash
   pip install -r requirements.txt
   ```

4. Configura la base de datos en `app/database/config.py`.

## Uso

1. Inicia la aplicación:

   ```bash
   uvicorn app.main:app --reload
   ```

2. Abre tu navegador y ve a `http://127.0.0.1:8000` para ver la documentación interactiva generada por Swagger.
