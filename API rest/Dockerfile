FROM python:3.8
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# Copiar el archivo requirements.txt
COPY requirements.txt .

# Instalar pip y dependencias
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# Copiar el resto del código al contenedor
COPY . .

# Exponer el puerto 8000 para acceder a la aplicación
EXPOSE 8000

# Ejecutar migraciones y luego iniciar el servidor de desarrollo
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
