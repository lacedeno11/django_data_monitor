# Implementation Plan

- [x] 1. Configurar ambiente de desarrollo Django
  - Crear y activar ambiente virtual con `python -m venv env`
  - Instalar Django con `pip install django`
  - Instalar requests con `pip install requests`
  - _Requirements: 1.1, 1.2, 1.3_

- [x] 2. Crear proyecto Django y aplicación dashboard
  - Crear proyecto Django llamado `backend_analytics_server` en ubicación actual
  - Crear aplicación `dashboard` con `python manage.py startapp dashboard`
  - Registrar aplicación dashboard en `INSTALLED_APPS` de settings.py
  - Configurar URLs para registrar dashboard en ruta raíz ("")
  - _Requirements: 1.1, 1.4_

- [x] 3. Configurar archivos estáticos en Django
  - Configurar `STATIC_URL = '/static/'` en settings.py
  - Configurar `STATICFILES_DIRS` apuntando a carpeta `static/`
  - Actualizar rutas estáticas en `templates/dashboard/base.html`
  - Reemplazar `./assets/css/tailwind.output.css` por `{% static 'css/tailwind.output.css' %}`
  - Reemplazar `./assets/js/init-alpine.js` por `{% static 'js/init-alpine.js' %}`
  - Reemplazar `./assets/js/charts-lines.js` por `{% static 'js/charts-Landing Page' Dashboard
Bienvenido al sistema de monitoreo de datos.js' %}`
  - _Requirements: 2.2, 2.3_

- [x] 4. Implementar vista básica del dashboard
  - Crear función `index` en `dashboard/views.py`
  - Importar `render` y `HttpResponse` de Django
  - Implementar renderización de plantilla `base.html`
  - Configurar URL en `dashboard/urls.py` para mapear vista a ruta raíz
  - Probar funcionamiento básico del servidor con `python manage.py runserver`
  - _Requirements: 2.1, 2.3, 2.4_

- [x] 5. Implementar herencia de plantillas
  - Modificar `templates/dashboard/base.html` para agregar bloque content
  - Encerrar sección actual entre `{% block content %}` y `{% endblock %}`
  - Crear plantilla `templates/dashboard/index.html`
  - Implementar extensión de base.html con `{% extends "dashboard/base.html" %}`
  - Definir bloque content con título de bienvenida "Landing Page' Dashboard"
  - Actualizar vista `index` para renderizar `dashboard/index.html`
  - _Requirements: 3.1, 3.2, 3.3, 3.4_

- [x] 6. Crear fragmentos de plantilla modulares
  - Crear directorio `templates/dashboard/partials/`
  - Crear directorio `templates/dashboard/content/`
  - Crear archivo `templates/dashboard/partials/header.html` con componente de encabezado
  - Crear archivo `templates/dashboard/content/data.html` con componente de datos
  - Modificar `templates/dashboard/index.html` para incluir fragmentos
  - Agregar `{% include "./partials/header.html" %}` y `{% include "./content/data.html" %}`
  - _Requirements: 4.1, 4.2, 4.3, 4.4_

- [ ] 7. Implementar renderización de datos del lado del servidor
  - Modificar `dashboard/views.py` para crear diccionario `data`
  - Agregar entrada `'title': "Landing Page' Dashboard"` al contexto
  - Pasar diccionario como contexto al renderizar plantilla index.html
  - Modificar `templates/dashboard/content/data.html` para usar variable `{{ title }}`
  - Reemplazar texto "Título Secundario" por `{{ title }}`
  - _Requirements: 5.1, 5.2, 5.3, 5.4_

- [ ] 8. Configurar integración con API externa
  - Agregar constante `API_URL = 'https://jsonplaceholder.typicode.com/posts'` en settings.py
  - Importar `requests` y `from django.conf import settings` en views.py
  - Implementar solicitud GET a JSONPlaceholder API en vista index
  - Procesar respuesta JSON con `response.json()`
  - Calcular `total_responses = len(posts)` y agregarlo al contexto
  - _Requirements: 6.1, 6.2, 6.3_

- [ ] 9. Mostrar métricas de API en dashboard
  - Modificar `templates/dashboard/content/data.html` para mostrar métricas
  - Reemplazar texto "Indicador 1" por "Número total de respuestas"
  - Reemplazar texto "Valor 1" por variable `{{ total_responses }}`
  - Probar funcionamiento completo del dashboard con datos de API
  - _Requirements: 6.4_

- [ ] 10. Configurar migraciones y superusuario
  - Ejecutar `python manage.py makemigrations` para generar migraciones
  - Ejecutar `python manage.py migrate` para aplicar migraciones a la base de datos
  - Crear superusuario con `python manage.py createsuperuser`
  - Verificar acceso al panel de administración en `/admin/`
  - Crear usuarios `usuario01` y `usuario02` sin permisos especiales

- [ ] 11. Configurar dominios y CSRF para desarrollo
  - Modificar `backend_analytics_server/settings.py` para agregar `CSRF_TRUSTED_ORIGINS`
  - Configurar `ALLOWED_HOSTS = ["*"]` para desarrollo
  - Agregar URLs para Codespaces: `"https://*.app.github.dev"`
  - Agregar URLs locales: `"https://localhost:8000"`, `"http://127.0.0.1:8000"`

- [ ] 12. Implementar autenticación con decorador @login_required
  - Modificar `dashboard/views.py` para importar `login_required`
  - Aplicar decorador `@login_required` a la vista `index`
  - Probar que el acceso al dashboard requiere autenticación
  - Verificar redirección al formulario de login cuando no está autenticado

- [ ] 13. Configurar vistas de autenticación
  - Crear directorio `templates/security/`
  - Crear archivo `templates/security/login.html` con formulario de login
  - Modificar `backend_analytics_server/urls.py` para importar `auth_views`
  - Agregar ruta `login/` con `LoginView` usando plantilla `security/login.html`
  - Agregar ruta `logout/` con `LogoutView` con redirección a `/login/`

- [ ] 14. Configurar constantes de autenticación
  - Modificar `backend_analytics_server/settings.py` para agregar `LOGIN_URL = '/login/'`
  - Agregar `LOGIN_REDIRECT_URL = '/'` para redirección después del login
  - Probar flujo de autenticación completo
  - Verificar redirección automática al dashboard después del login exitoso

- [ ] 15. Implementar formulario de inicio de sesión
  - Modificar `templates/security/login.html` para agregar `method="post"`
  - Agregar `action="{% url 'login' %}"` al formulario
  - Incluir token CSRF con `{% csrf_token %}`
  - Agregar atributo `name="username"` al campo de usuario
  - Agregar atributo `name="password"` al campo de contraseña
  - Probar autenticación con superusuario, usuario01 y usuario02

- [ ] 16. Implementar formulario de cierre de sesión
  - Modificar `templates/dashboard/partials/header.html` en bloque logout
  - Agregar formulario con `method="post"` y `action="{% url 'logout' %}"`
  - Incluir token CSRF en formulario de logout
  - Probar que el logout redirige correctamente al formulario de login
  - Verificar que la cookie de sesión se elimina correctamente

- [ ] 17. Implementar verificación de acceso y mensajes de error
  - Modificar `templates/security/login.html` para mostrar errores de formulario
  - Agregar `{% if form.non_field_errors %}` para mostrar mensaje de error
  - Mostrar mensaje "Invalid username or password." en caso de error
  - Modificar `templates/dashboard/partials/header.html` para mostrar username
  - Agregar `{% if user.is_authenticated %}` para mostrar `{{ user.username }}`

- [ ] 18. Implementar manejo básico de errores de API
  - Agregar try-catch para manejar errores de conexión a API
  - Implementar valores por defecto cuando API no esté disponible
  - Agregar logging básico para errores de API
  - _Requirements: 6.5_

- [ ] 19. Generar documentación de dependencias actualizada
  - Ejecutar `pip freeze > requirements.txt` para incluir todas las dependencias
  - Verificar que requirements.txt incluya Django, requests y otras dependencias
  - Documentar proceso de instalación y configuración en README.md
  - Incluir instrucciones para migraciones y creación de superusuario
  - _Requirements: 7.1, 7.4_

- [ ] 20. Configurar versionado con Git
  - Inicializar repositorio Git si no existe
  - Crear archivo .gitignore con plantilla de Python
  - Agregar db.sqlite3 y __pycache__/ al .gitignore
  - Hacer commit inicial con estructura base del proyecto
  - Crear rama de desarrollo para cambios de autenticación
  - _Requirements: 7.2, 7.3_

- [ ] 21. Configurar PyMySQL para conexión MySQL
  - Instalar PyMySQL en el ambiente virtual con `pip install PyMySQL`
  - Importar PyMySQL en settings.py y ejecutar `pymysql.install_as_MySQLdb()`
  - Reemplazar configuración de base de datos por MySQL usando variables de entorno
  - Establecer variables de entorno: MYSQLDATABASE, MYSQLUSER, MYSQLPASSWORD, MYSQLHOST, MYSQLPORT
  - Crear base de datos MySQL 'security' si no existe
  - _Requirements: 8.1_

- [ ] 22. Configurar migraciones con base de datos MySQL
  - Ejecutar `python manage.py makemigrations` con nueva configuración
  - Ejecutar `python manage.py migrate` para aplicar migraciones a MySQL
  - Crear superusuario con `python manage.py createsuperuser`
  - Crear usuarios 'usuario01' y 'usuario02' sin permisos especiales
  - Verificar redirección a login cuando no autenticado
  - _Requirements: 8.2_

- [ ] 23. Implementar autorización con decorador @permission_required
  - Importar `permission_required` en dashboard/views.py
  - Aplicar decorador `@permission_required('dashboard.index_viewer', raise_exception=True)` a vista index
  - Verificar que superusuario tiene acceso sin restricciones
  - Comprobar que usuario01 y usuario02 requieren permisos específicos
  - _Requirements: 8.3_

- [ ] 24. Crear modelo con permisos personalizados
  - Crear clase `DashboardModel` en dashboard/models.py
  - Definir permisos personalizados en Meta class con "index_viewer"
  - Generar y aplicar migraciones para el nuevo modelo
  - Verificar creación de permisos en base de datos
  - _Requirements: 8.4_

- [ ] 25. Configurar permisos de usuario en Django Admin
  - Acceder al panel de administración Django en /admin/
  - Modificar usuario 'usuario01' para agregar permiso "Can show to index view"
  - Dejar usuario 'usuario02' sin permisos especiales
  - Probar acceso: usuario01 (permitido), usuario02 (403), superusuario (permitido)
  - _Requirements: 8.5_

- [ ] 26. Implementar página personalizada 403 Forbidden
  - Crear archivo `templates/403.html` con diseño de error personalizado
  - Configurar Django para usar plantilla personalizada en errores 403
  - Probar que usuario02 ve página 403 personalizada al acceder sin permisos
  - Verificar que la página mantiene el diseño consistente del sitio
  - _Requirements: 8.6_

- [ ] 27. Actualizar gestión de dependencias con PyMySQL
  - Ejecutar `pip freeze > requirements.txt` para incluir PyMySQL
  - Verificar que requirements.txt incluya PyMySQL y todas las dependencias
  - Documentar configuración de variables de entorno en README.md
  - Incluir instrucciones para configuración de base de datos MySQL
  - _Requirements: 8.7_

- [ ] 28. Versionado final con autorización implementada
  - Crear rama de desarrollo para implementación de autorización
  - Commitear cambios de PyMySQL, permisos y modelo DashboardModel
  - Generar pull request para revisión de cambios de autorización
  - Documentar proceso de configuración de permisos y usuarios
  - _Requirements: 8.8_