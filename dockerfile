FROM python:3.10

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requerimientos y los instala
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia el resto del código del proyecto
COPY . .

# Exponer el puerto de Django (8000)
EXPOSE 8000

# Ejecuta las migraciones y levanta el servidor de desarrollo
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
