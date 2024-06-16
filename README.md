# TO-DO-APP-DJANGO
By Edgar Ortega

## Descripción
Bienvenido a To Do App, una aplicación de gestión de tareas desarrollada con Django. Este proyecto tiene como objetivo proporcionar a los usuarios una herramienta sencilla y eficaz para organizar sus actividades diarias. Con un diseño minimalista y responsivo, To Do App garantiza una experiencia de usuario fluida gracias a la concepción de su diseño.

To Do App presenta las siguientes funcionalidades:

- **Formulario de registro:** Los usuarios pueden crear cuentas personalizadas para gestionar sus tareas de manera segura y privada. El proceso de registro es sencillo e intuitivo.
- **Inicio de Sesión:** Accede a tu cuenta de manera rápida y segura. La autenticación de usuarios garantiza que solo tú puedas ver y gestionar tus tareas.
- **Gestión de Tareas:** Añade, edita y elimina tareas con facilidad. Organiza tus tareas por prioridad y fecha de vencimiento para mantenerte al día con tus responsabilidades.
- **Confirmación de eliminación:** Formulario para validar tareas eliminadas.

---

## Estructura del Proyecto

### Paso a paso del proyecto

#### Step 1: Configuraciones del entorno de desarrollo

1. Crear carpeta del proyecto en local `PI-Django-ToDoList`. Todo trabajo a partir de este punto se realiza en el directorio del proyecto.
2. Inicialización del repositorio local y vinculación con repositorio remoto en GitHub:
    ```sh
    git init
    git add .
    git commit -m 'Repository initialization'
    git branch -M main
    git remote add origin <url_repository_github>
    git push -u origin main
    ```
3. Creación y activación de ambiente virtual de trabajo:
    ```sh
    pip install virtualenv
    python -m venv venv
    .\venv\Scripts\activate    
    ```
4. Instalación del framework Django:
    ```sh
    pip install django
    ```
5. Creación del archivo de dependencias `requirements.txt`:
    ```sh
    pip freeze > requirements.txt
    ```
6. Creación del archivo `.gitignore` y adición de archivos y directorios ignorados: directorio `venv`, archivo `.gitignore`.
7. Creación del proyecto Django `todo_list`:
    ```sh
    django-admin startproject todo_list
    ```
8. Creación de nueva aplicación dentro del proyecto:
    ```sh
    cd base  # Cambia al sub-directorio para trabajos de desarrollo
    python manage.py startapp base
    ```

#### Step 2: Diseño del modelo de datos

1. Configuración de la aplicación creada en el archivo `todo_list\settings.py`:
    ```python
    INSTALLED_APPS = [
        ...,
        'base.apps.BaseConfig', 
    ]
    ```
2. Crear archivo `urls.py` en `base\urls.py` y definir las URLs para cada vista creada en `base\views.py`.

#### Step 3: Implementación de funcionalidades

1. Crear vistas en `base\views.py` para realizar las operaciones CRUD (crear, leer, actualizar, eliminar tareas).
2. Definir las funciones de vista para cada operación CRUD:
    - Inicio de sesión
    - Registro
    - Lista de tareas
    - Detalle de tareas
    - Crear tarea
    - Actualización de tarea
    - Eliminar tarea

#### Step 4: Diseño de la Interfaz de Usuario

1. Utilizar Django Templates para diseñar las plantillas HTML en la carpeta `templates\base`.
2. Estilizar la interfaz y hacerla responsiva en la ruta `static\base\styles.css`.

#### Step 5: Configuración de Django Admin

1. Registrar el modelo `Task` en `base\admin.py` para poder administrarlo desde Django Admin:
    ```python
    from django.contrib import admin
    from .models import Task

    admin.site.register(Task)
    ```
2. Crear superusuario en Django:
    ```sh
    python manage.py createsuperuser
    ```

#### Step 6: Ejecución y Pruebas

1. Ejecutar el servidor de desarrollo de Django:
    ```sh
    python manage.py runserver
    ```
2. Acceder a la aplicación desde tu navegador y realizar pruebas para asegurarte de que todas las funcionalidades funcionen correctamente.

---

## Mejoras y Adiciones Futuras

- Integración con servicios de terceros para notificaciones.
- Implementación de recordatorios para las tareas.
- Mejora de la interfaz de usuario con más opciones de personalización.

---

## Contacto
Para cualquier consulta o sugerencia, por favor contacta a [Tu Nombre] a través de [tu.email@example.com].
