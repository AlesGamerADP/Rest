## Django API REST - CRUD de Personas

Este es un proyecto básico de una API REST utilizando Django y Django REST Framework. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre un modelo Persona. El proyecto también incluye filtrado y búsqueda avanzada de las personas.

Requisitos

  * Python 3.x

  * Django 3.x o superior

  * Django REST Framework

  * Django Filters (para filtrado en la API)

# Instalación

1. Clonar el repositorio
```
git clone https://github.com/tu-usuario/tu-repositorio.git

cd tu-repositorio
```
2. Crear un entorno virtual
```
python -m venv venv

venv\Scripts\activate
```
3. Instalar dependencias
``` 
pip install -r requirements.txt

En caso que no se instalen todas las dependencias 

pip install django

pip install django djangorestframework

pip install django-filter
```
4. Crear base de datos y aplicar migraciones
```
python manage.py migrate
```
5. Crear un superusuario
```
python manage.py createsuperuser
```
6. Ejecutar el servidor de desarrollo
````
python manage.py runserver
````

# URLs de la Api

Las rutas de la API están definidas en el archivo crud/urls.py. Estas rutas permiten interactuar con las personas mediante las siguientes operaciones:

+ Pagina de Inicio de Api Root : http://127.0.0.1:8000/

+ Crear una persona: POST /api/persona/create/

+ Obtener detalles de una persona: GET /api/persona/{id}/

+ Actualizar una persona: PUT /api/persona/update/{id}/

+ Eliminar una persona: DELETE /api/persona/delete/{id}/

+ Contar el total de personas: GET /api/persona/count/

+ Filtrar personas: GET /api/filter_personas/

+ Buscar personas: GET /api/list_personas/

















































