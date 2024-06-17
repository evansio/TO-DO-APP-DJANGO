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


### Requisitos

- Python 3.8+
- Django 3.2+

### Paso 1: Clonar el repositorio

## Instrucciones para Configurar y Ejecutar el Proyecto en Visual Studio Code

### Paso 1: Clonar el Repositorio

1. Abre Visual Studio Code.
2. Abre una terminal integrada en VSCode (Ctrl + `).
3. Clona el repositorio desde GitHub:

```bash
git clone https://github.com/tu_usuario/todoproject.git
cd todoproject

Paso 2: Crear y Activar un Entorno Virtual
En la terminal integrada de VSCode, crea un entorno virtual:
bash
Copiar código
python -m venv env

Paso 3: Instalar las dependencias
bash
Copiar código
pip install -r requirements.txt
Paso 4: Realizar las migraciones de la base de datos
bash
Copiar código
python manage.py migrate
Paso 5: Crear un superusuario
bash
Copiar código
python manage.py createsuperuser
Paso 6: Ejecutar el servidor de desarrollo
bash
Copiar código
python manage.py runserver
Ahora puedes acceder al proyecto en http://127.0.0.1:8000.

Descripción de la Estructura del Proyecto
Directorios y Archivos Principales
todoproject/: Contiene la configuración principal del proyecto.
settings.py: Configuraciones del proyecto Django.
urls.py: Configuración de las URL principales.
tasks/: Aplicación de gestión de tareas.
models.py: Define el modelo Task.
views.py: Contiene las vistas para listar, crear, editar y eliminar tareas.
urls.py: Configuración de las URL específicas de la aplicación de tareas.
forms.py: Define el formulario TaskForm.
templates/tasks/: Contiene las plantillas HTML para las vistas.
Decisiones de Diseño Importantes
Estructura del Modelo:

El modelo Task incluye campos para el título, descripción, fecha de creación, estado (pendiente o completado) y el usuario propietario de la tarea.
Autenticación y Autorización:

Se utiliza el sistema de autenticación de Django para gestionar el acceso de los usuarios. Las vistas están protegidas con @login_required para asegurarse de que solo los usuarios autenticados puedan acceder a ellas.
Interfaz de Usuario:

Se han utilizado iconos de Font Awesome para mejorar la interfaz de usuario, sustituyendo botones de texto por iconos intuitivos.
Estilos y Diseño:

Se ha añadido una hoja de estilos CSS personalizada para mejorar la apariencia visual de la aplicación.
Funcionalidad de Tareas:

Los usuarios pueden crear, editar, eliminar y marcar tareas como completadas o pendientes.
Las tareas completadas se muestran con una opacidad reducida para diferenciarlas visualmente.
Contacto
Para cualquier duda o sugerencia, puedes contactar a [tu correo electrónico].

shell
Copiar código

### 4. Requisitos del Proyecto

Crea un archivo `requirements.txt` con las dependencias necesarias:

#### requirements.txt

Django==3.2.14

shell
Copiar código

### 5. Asegúrate de que todo funciona correctamente

Antes de subir el proyecto, asegúrate de que todo funciona correctamente ejecutando el servidor y probando las funcionalidades principales.

### 6. Subir el Proyecto a un Repositorio

Sube todo el proyecto a un repositorio en GitHub o cualquier otra plataforma de control de versiones que prefieras.

### 7. Instrucciones para el Usuario

En el archivo `README.md` ya se han incluido las instrucciones para configurar y ejecutar el proyecto. Asegúrate de que sean claras y fáciles de seguir.

Con estos pasos, tendrás un paquete completo de tu proyecto con la documentación adecuada para configurar, ejecutar y entender la estructura y las decisiones de diseño.
Me esta arrojando el siguiente error:

## Mejoras y Adiciones Futuras

- Integración con servicios de terceros para notificaciones.
- Implementación de recordatorios para las tareas.
- Mejora de la interfaz de usuario con más opciones de personalización.

---

## Contacto
Para cualquier consulta o sugerencia, por favor contacta a [Tu Nombre] a través de [tu.email@example.com].
