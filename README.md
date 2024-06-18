# TO-DO-APP-DJANGO
By Edgar Ortega

## Descripción
Bienvenido a To Do App, una aplicación de gestión de tareas desarrollada con Django. Este proyecto tiene como objetivo proporcionar a los usuarios una herramienta sencilla y eficaz para organizar sus actividades diarias. Con un diseño minimalista y responsivo, To Do App garantiza una experiencia de usuario fluida gracias a la concepción de su diseño.

To Do App presenta las siguientes funcionalidades:

- **Formulario de registro:** Los usuarios pueden crear cuentas personalizadas para gestionar sus tareas de manera segura y privada. El proceso de registro es sencillo e intuitivo.
- **Inicio de Sesión:** Accede a tu cuenta de manera rápida y segura. La autenticación de usuarios garantiza que solo tú puedas ver y gestionar tus tareas.
- **Gestión de Tareas:** Añade, edita y elimina tareas con facilidad. Organiza tus tareas por prioridad y fecha de vencimiento para mantenerte al día con tus responsabilidades.
---

<img width="410" alt="app_todo_project_denisse" src="https://github.com/evansio/TO-DO-APP-DJANGO/assets/99567473/ee0fb870-b4f0-471c-8374-816a49cb544c">


## Estructura del Proyecto
<img width="172" alt="Estructura del Proyecto" src="https://github.com/evansio/TO-DO-APP-DJANGO/assets/99567473/2f978c4f-9ef6-4961-87cf-7939da1ab3bb">


## Requisitos

- asgiref==3.8.1
- Django==5.0.6
- sqlparse==0.5.0
- tzdata==2024.1

## Instrucciones para Configurar y Ejecutar el Proyecto en Visual Studio Code

### Paso 1: Clonar el Repositorio

1. Abre Visual Studio Code.
2. Abre una terminal integrada en VSCode (Ctrl + `).
3. Clona el repositorio desde GitHub:

```bash
git clone https://github.com/evansio/TO-DO-APP-DJANGO.git
cd TO-DO-APP-DJANGO
```
### Paso 2: Crear archivo README.md
Asegúrate de que tu README.md contenga instrucciones claras para la configuración y ejecución del proyecto.

### Paso 3: Crear y Activar un Entorno Virtual
En la terminal integrada de VSCode, crea un entorno virtual:

```bash
 pip install virtualenv
 python -m venv venv
 .\venv\Scripts\activate
```
### Paso 4: Instalar Django
```bash
pip install django
```

### Paso 5: Instalar las dependencias
```bash
pip freeze > requirements.txt
```
### Paso 6: Crear un superusuario
```bash
python manage.py createsuperuser
```
### Paso 7: Ejecutar el servidor de desarrollo
```bash
python manage.py runserver
```
Ahora puedes acceder al proyecto en http://127.0.0.1:8000.

## Descripción de la Estructura del Proyecto
### Directorios y Archivos Principales
#### todoproject/: Contiene la configuración principal del proyecto.
#### settings.py: Configuraciones del proyecto Django.
#### urls.py: Configuración de las URL principales.
#### tasks/: Aplicación de gestión de tareas.
#### models.py: Define el modelo Task.
#### views.py: Contiene las vistas para listar, crear, editar y eliminar tareas.
#### urls.py: Configuración de las URL específicas de la aplicación de tareas.
#### forms.py: Define el formulario TaskForm.
#### templates/tasks/: Contiene las plantillas HTML para las vistas.

## Decisiones de Diseño Importantes

### Estructura del Modelo:

El modelo Task incluye campos para el título, descripción, fecha de creación, estado (pendiente o completado) y el usuario propietario de la tarea.

### Autenticación y Autorización:

Se utiliza el sistema de autenticación de Django para gestionar el acceso de los usuarios. Las vistas están protegidas con @login_required para asegurarse de que solo los usuarios autenticados puedan acceder a ellas.

### Interfaz de Usuario:

Se han utilizado iconos de Font Awesome para mejorar la interfaz de usuario, sustituyendo botones de texto por iconos intuitivos.

### Estilos y Diseño:

Se ha añadido una hoja de estilos CSS personalizada para mejorar la apariencia visual de la aplicación.

### Funcionalidad de Tareas:

- Los usuarios pueden crear, editar, eliminar y marcar tareas como completadas o pendientes.
- Las tareas completadas se muestran con una opacidad reducida para diferenciarlas visualmente.

## Mejoras y Adiciones Futuras

- Integración con servicios de terceros para notificaciones.
- Implementación de recordatorios para las tareas.
- Mejora de la interfaz de usuario con más opciones de personalización.

---

## Contacto
Para cualquier consulta o sugerencia, por favor contacta a Edgar Ortega a través de [edgarortega1991@gmail.com].
