# Django Data Monitor - Analytics Dashboard

## 🚀 Deploy en Railway

### 1. Preparación del Proyecto
Todos los archivos ya están configurados para Railway:
- ✅ `requirements.txt` con todas las dependencias
- ✅ `railway.toml` configurado
- ✅ `Procfile` con comandos de inicio
- ✅ `settings.py` optimizado para producción
- ✅ Tailwind CSS compilado

### 2. Variables de Entorno en Railway
En el Dashboard de Railway, configura estas variables:

**Base de Datos MySQL (Railway las proporciona automáticamente):**
```
MYSQLDATABASE=railway
MYSQLUSER=root  
MYSQLPASSWORD=tu_password_aqui
MYSQLHOST=containers-us-west-xxx.railway.app
MYSQLPORT=7XXX
```

**Django Settings:**
```
DEBUG=False
SECRET_KEY=tu_secret_key_seguro_aqui
```

### 3. Comandos de Deploy
```bash
# 1. Agregar cambios a git
git add .
git commit -m "Deploy to Railway - Dashboard completo"

# 2. Push a Railway (conecta tu repo en Railway Dashboard)
git push origin main
```

### 4. Post-Deploy en Railway
Una vez deployado, ejecuta en Railway Shell:
```bash
python create_superuser.py
```

### 5. Credenciales por Defecto
- **Admin**: `admin` / `admin123`
- **Usuario normal**: `usuario` / `password123`

### 6. URLs del Proyecto
- **Dashboard**: `https://tu-app.railway.app/`
- **Admin Panel**: `https://tu-app.railway.app/admin/`
- **Login**: `https://tu-app.railway.app/login/`

## 🛠️ Desarrollo Local

### Instalación
```bash
# 1. Clonar repositorio
git clone <tu-repo>
cd django_data_monitor

# 2. Crear entorno virtual
python -m venv env
source env/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar base de datos local
python manage.py migrate

# 5. Crear superusuario
python manage.py createsuperuser

# 6. Recopilar archivos estáticos
python manage.py collectstatic

# 7. Ejecutar servidor
python manage.py runserver
```

### Compilar Tailwind CSS
```bash
# Para desarrollo (con watch)
npm run build-css

# Para producción (minificado)
npm run build-css-prod
```

## 📁 Estructura del Proyecto
```
├── backend_analytics_server/    # Configuración Django
├── dashboard/                   # App principal
├── templates/                   # Templates HTML
├── static/                      # Archivos estáticos
├── requirements.txt            # Dependencias Python
├── railway.toml               # Configuración Railway
├── Procfile                   # Comandos de inicio
└── create_superuser.py        # Script para usuarios
```

## 🎯 Funcionalidades
- ✅ Dashboard analítico con métricas en tiempo real
- ✅ Gráficos interactivos con Chart.js
- ✅ Autenticación y control de acceso
- ✅ Interfaz responsive con Tailwind CSS
- ✅ Integración con API externa (JSONPlaceholder)
- ✅ Sistema de permisos por grupos
- ✅ Página 403 personalizada
- ✅ Panel de administración Django

## 🔧 Tecnologías
- **Backend**: Django 5.2.4
- **Base de Datos**: MySQL (Railway), SQLite (local)
- **Frontend**: Tailwind CSS + Alpine.js
- **Gráficos**: Chart.js
- **Deploy**: Railway
- **Server**: Gunicorn + WhiteNoise