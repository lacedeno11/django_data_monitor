# Django Data Monitor

## Descripción del Proyecto

Django Data Monitor es un backend desarrollado con Django que permite monitorear y gestionar datos en tiempo real. Este proyecto proporciona una API robusta para el seguimiento de métricas, análisis de datos y generación de reportes.

### Características principales:
- Monitoreo de datos en tiempo real
- API RESTful para integración con frontend
- Sistema de autenticación y autorización
- Dashboard administrativo
- Generación de reportes y métricas

## Instalación y Configuración

### Prerrequisitos
- Python 3.8+
- pip
- virtualenv

### Configuración del ambiente de desarrollo

1. Clonar el repositorio:
```bash
git clone https://github.com/[tu-usuario]/django_data_monitor.git
cd django_data_monitor
```

2. Crear y activar el ambiente virtual:
```bash
python -m venv env
# Windows
env\Scripts\activate
# Linux/MacOS
source env/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecutar migraciones:
```bash
python manage.py migrate
```

5. Crear superusuario:
```bash
python manage.py createsuperuser
```

6. Ejecutar el servidor de desarrollo:
```bash
python manage.py runserver
```

## Uso

El servidor estará disponible en `http://localhost:8000/`

## Contribución

1. Crear una rama de desarrollo
2. Realizar cambios
3. Enviar pull request

## Licencia

Este proyecto está bajo la Licencia MIT.
