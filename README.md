# Django Data Monitor

Backend analytics server con Django que incluye un dashboard para monitorear datos en tiempo real.

## Características

- **Dashboard de Análisis**: Interfaz web moderna con métricas en tiempo real
- **Integración con APIs Externas**: Consumo de datos desde JSONPlaceholder API
- **Sistema de Autenticación**: Login/logout con Django Auth
- **Panel de Administración**: Gestión de usuarios mediante Django Admin
- **Responsive Design**: Interfaz adaptable con Tailwind CSS
- **Server Side Rendering**: Renderización del lado del servidor con herencia de plantillas

## Tecnologías

- **Backend**: Django 5.2.4
- **Frontend**: HTML5, Tailwind CSS, Alpine.js
- **Base de Datos**: SQLite (desarrollo)
- **APIs**: JSONPlaceholder para datos de prueba

## Instalación

### Prerrequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Configuración del Proyecto

1. **Crear ambiente virtual**
   ```bash
   python -m venv env
   ```

2. **Activar ambiente virtual**
   ```bash
   # En macOS/Linux
   source env/bin/activate
   
   # En Windows
   env\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar base de datos**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crear superusuario**
   ```bash
   python manage.py createsuperuser
   ```

6. **Iniciar servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

## Uso

### Acceso al Sistema

- **Dashboard Principal**: http://127.0.0.1:8000/
- **Panel de Administración**: http://127.0.0.1:8000/admin/
- **Login**: http://127.0.0.1:8000/login/

### Usuarios de Prueba

El sistema incluye los siguientes usuarios para testing:

| Usuario | Contraseña | Permisos |
|---------|------------|----------|
| abrahan | admin123 | Superusuario |
| usuario01 | password123 | Usuario regular |
| usuario02 | password123 | Usuario regular |

### Funcionalidades

1. **Dashboard de Métricas**
   - Total de posts desde API externa
   - Información en tiempo real
   - Interfaz responsive

2. **Sistema de Autenticación**
   - Login con credenciales
   - Logout seguro con CSRF protection
   - Redirección automática

3. **Panel de Administración**
   - Gestión de usuarios
   - Configuración del sistema
   - Solo accesible para superusuarios

## Estructura del Proyecto

```
django_data_monitor/
├── backend_analytics_server/    # Configuración principal de Django
├── dashboard/                   # Aplicación principal del dashboard
├── static/                      # Archivos estáticos (CSS, JS, imágenes)
├── templates/                   # Plantillas HTML
│   ├── dashboard/              # Plantillas del dashboard
│   └── security/               # Plantillas de autenticación
├── env/                        # Ambiente virtual
├── manage.py                   # Script de gestión de Django
└── requirements.txt            # Dependencias del proyecto
```

## API Externa

El sistema consume datos de **JSONPlaceholder** (https://jsonplaceholder.typicode.com/posts) para mostrar métricas en tiempo real. En caso de que la API no esté disponible, el sistema mostrará valores por defecto.

## Desarrollo

### Comandos Útiles

```bash
# Activar ambiente virtual
source env/bin/activate

# Instalar nueva dependencia
pip install <package>
pip freeze > requirements.txt

# Crear nueva aplicación
python manage.py startapp <app_name>

# Realizar migraciones
python manage.py makemigrations
python manage.py migrate

# Recopilar archivos estáticos (producción)
python manage.py collectstatic

# Crear superusuario
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver
```

### Configuración de Desarrollo

El proyecto está configurado para desarrollo con:

- `DEBUG = True`
- `ALLOWED_HOSTS = ["*"]`
- CSRF trusted origins para localhost y Codespaces
- SQLite como base de datos

### Seguridad

- Autenticación requerida para acceso al dashboard
- Protección CSRF en todos los formularios
- Hashing seguro de contraseñas con Django
- Manejo de errores de API

## Soporte

Para reportar problemas o solicitar nuevas funcionalidades, crear un issue en el repositorio del proyecto.
