# Proyecto de Gestión de Vehiculos

Este proyecto es una aplicación web para gestionar una concesionaria de autos. Permite la administración de vehículos, marcas, reseñas de vehículos, clientes y usuarios. Además, ofrece una API RESTful para realizar operaciones de consulta y modificación a través de endpoints seguros, con autenticación basada en tokens.

## Características del Proyecto

- **Gestión de Vehículos**: CRUD completo para gestionar los vehículos en la concesionaria.
- **Gestión de Marcas**: CRUD para las marcas de vehículos.
- **Gestión de Clientes y Usuarios**: CRUD para clientes, con control de acceso para usuarios `staff`.
- **Reseñas de Vehículos**: Los usuarios autenticados pueden agregar y ver reseñas de los vehículos.
- **API RESTful**: Se exponen endpoints para realizar consultas y modificaciones a través de una API documentada con Swagger.

## Tecnologías Utilizadas

- **Backend**: Django, Django REST Framework
- **Frontend**: Bootstrap para los estilos en las plantillas HTML
- **Base de Datos**: PostgreSQL
- **Autenticación**: Tokens de autenticación con `TokenAuthentication`
- **Documentación de la API**: Generada automáticamente con `drf-yasg`

## Instalación

1. **Clona el Repositorio**:
   ```bash
   git clone https://github.com/lucassalzotto-dat/gestion_vehiculos.git
   cd gestion_vehiculos
   ```

2. **Crea un Entorno Virtual e Instala las Dependencias**:
   ```bash
   python -m venv env
   source env/bin/activate  # En Windows usa: env\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configura la Base de Datos**:
   - Crea una base de datos en PostgreSQL.
   - Actualiza las credenciales de acceso en `settings.py` en la sección `DATABASES`.

4. **Realiza las Migraciones**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crea un Superusuario**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Corre el Servidor**:
   ```bash
   python manage.py runserver
   ```

## Uso de la Aplicación

### 1. Interfaz Web

- Accede a la interfaz principal en `http://127.0.0.1:8000/`.
- Usa la cuenta de `superusuario` para iniciar sesión y administrar los datos.
- Navega por las secciones para gestionar vehículos, marcas, clientes y reseñas.

### 2. Documentación de la API

- La documentación de la API está disponible en formato Swagger.
- Accede a ella en [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/).
- Puedes explorar todos los endpoints disponibles y realizar pruebas directamente desde la interfaz de Swagger.

### 3. Pruebas de la API en Postman

- Puedes usar herramientas como **Postman** o **cURL** para interactuar con la API.
- Asegúrate de incluir el token de autenticación en el encabezado `Authorization` en el formato `Token <tu_token>` para los endpoints que requieren autenticación.

## Licencia

Valentín Hildmann & Lucas Salzotto

