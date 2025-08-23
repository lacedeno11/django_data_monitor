# 🚀 Guía de Despliegue en Railway

## ✅ Estado Actual del Proyecto

**COMPLETADO:**
- ✅ Corrección completa del frontend (Tailwind CSS + Alpine.js + Chart.js)
- ✅ Sistema de autenticación con grupos de usuarios
- ✅ Configuración de producción para Railway con MySQL
- ✅ Archivos estáticos configurados con whitenoise
- ✅ Scripts de creación de usuarios
- ✅ Código empujado al repositorio GitHub

## 📋 Pasos para Desplegar en Railway

### 1. Conectar Repositorio a Railway

1. Ve a [Railway.app](https://railway.app) e inicia sesión
2. Haz clic en **"New Project"**
3. Selecciona **"Deploy from GitHub repo"**
4. Conecta tu repositorio: `lacedeno11/django_data_monitor`
5. Selecciona la rama **`produccion`**

### 2. Configurar Variables de Entorno

En el dashboard de Railway, ve a **Variables** y añade:

```env
# Configuración Django
DEBUG=False
SECRET_KEY=tu-clave-secreta-super-segura-aqui
ALLOWED_HOSTS=.railway.app,.up.railway.app

# Base de datos MySQL
MYSQL_ROOT_PASSWORD=password-seguro-mysql
MYSQL_DATABASE=django_data_monitor
MYSQL_USER=django_user
MYSQL_PASSWORD=password-seguro-django
MYSQL_HOST=mysql
MYSQL_PORT=3306

# URL de base de datos (Railway la creará automáticamente)
DATABASE_URL=mysql://usuario:password@host:puerto/database

# Configuración adicional
PORT=8000
PYTHONPATH=/app
```

### 3. Añadir Servicio MySQL

1. En tu proyecto Railway, haz clic en **"+ New Service"**
2. Selecciona **"Database"**
3. Elige **"MySQL"**
4. Railway creará automáticamente las variables de conexión

### 4. Configurar Dominio Personalizado (Opcional)

1. Ve a **Settings > Domains**
2. Haz clic en **"Generate Domain"** para obtener un dominio `.railway.app`
3. O añade tu dominio personalizado

### 5. Verificar Despliegue

El despliegue debería iniciar automáticamente. Puedes monitorear:

1. **Logs de construcción** en la pestaña **"Deployments"**
2. **Logs de aplicación** en tiempo real
3. Estado del servicio en el dashboard

## 🔧 Scripts de Post-Despliegue

### Crear Superusuario en Producción

Una vez desplegado, ejecuta desde la consola de Railway:

```bash
python create_superuser.py
```

Esto creará:
- **Superusuario:** `admin` / `admin123`
- **Usuario normal:** `usuario` / `password123`
- **Grupos de permisos** configurados

### Ejecutar Migraciones

```bash
python manage.py migrate
python manage.py collectstatic --noinput
```

## 🎯 URLs de Acceso

### Desarrollo Local
- **Dashboard:** http://localhost:8000/dashboard/
- **Login:** http://localhost:8000/login/
- **Admin:** http://localhost:8000/admin/

### Producción Railway
- **Dashboard:** https://tu-app.railway.app/dashboard/
- **Login:** https://tu-app.railway.app/login/
- **Admin:** https://tu-app.railway.app/admin/

## 👥 Usuarios de Prueba

### Superusuario (Acceso completo)
- **Usuario:** `admin`
- **Contraseña:** `admin123`
- **Permisos:** Acceso total al dashboard y panel de administración

### Usuario Normal (Acceso limitado)
- **Usuario:** `usuario`
- **Contraseña:** `password123`
- **Permisos:** Solo visualización del dashboard

## 🔍 Verificaciones de Funcionamiento

### ✅ Frontend
- [ ] Tailwind CSS se carga correctamente
- [ ] Menús interactivos funcionan (Alpine.js)
- [ ] Gráficos se muestran con datos (Chart.js)
- [ ] Tema oscuro/claro funcional

### ✅ Backend
- [ ] Login y autenticación funcionan
- [ ] Dashboard muestra métricas correctas
- [ ] Permisos por grupos funcionan
- [ ] Base de datos MySQL conectada

### ✅ Datos de Prueba
El dashboard mostrará:
- **Total de respuestas:** 1,247
- **Emails únicos:** 892
- **Quieren más info:** 456
- **Fuentes únicas:** 23
- **Gráfico de líneas** con datos de los últimos 30 días

## 🚨 Troubleshooting

### Problema: CSS no se carga
**Solución:** Verificar que whitenoise esté configurado y `collectstatic` ejecutado

### Problema: Error de conexión a BD
**Solución:** Verificar variables de entorno MySQL en Railway

### Problema: 403 Forbidden
**Solución:** Verificar `ALLOWED_HOSTS` incluye dominio de Railway

### Problema: Gráficos no aparecen
**Solución:** Verificar que Chart.js se carga y datos llegan al frontend

## 📞 Contacto

Si necesitas ayuda adicional:
1. Revisa los logs en Railway Dashboard
2. Verifica las variables de entorno
3. Ejecuta los scripts de post-despliegue

¡Tu aplicación Django está lista para producción! 🎉
