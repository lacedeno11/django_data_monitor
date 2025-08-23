# Configuración adicional para Railway - Archivos Estáticos
# Este archivo contiene configuraciones específicas para Railway

## Configuraciones aplicadas en settings.py:

### 1. STATICFILES_STORAGE
- **Desarrollo**: `django.contrib.staticfiles.storage.StaticFilesStorage`
- **Producción**: `whitenoise.storage.CompressedManifestStaticFilesStorage`

### 2. MIDDLEWARE
- `whitenoise.middleware.WhiteNoiseMiddleware` debe estar después de `SecurityMiddleware`

### 3. Variables de entorno críticas para Railway:
- `DEBUG=False` (automático cuando `MYSQLDATABASE` está presente)
- `STATIC_ROOT=/app/staticfiles` (en Railway)
- `STATIC_URL=/static/`

### 4. Comando de deploy en railway.toml:
```
python manage.py collectstatic --noinput --clear && gunicorn backend_analytics_server.wsgi:application
```

### 5. Archivos críticos que deben servirse:
- `/static/css/tailwind.output.css` - Estilos principales
- `/static/js/init-alpine.js` - JavaScript de Alpine.js
- `/static/js/charts-lines.js` - Gráficos Chart.js
- `/static/img/*` - Imágenes del dashboard

### 6. Configuraciones Whitenoise aplicadas:
- `WHITENOISE_SKIP_COMPRESS_EXTENSIONS` - Para archivos ya comprimidos
- `WHITENOISE_MAX_AGE` - Cache por 1 año
- Compresión y manifest habilitados para mejor rendimiento

### 7. Solución al problema 404:
El problema principal era el uso de `StaticFilesStorage` en producción.
Whitenoise requiere `CompressedManifestStaticFilesStorage` para servir
archivos correctamente desde `STATIC_ROOT`.

### 8. Verificación:
Los archivos estáticos se copian a `/app/staticfiles/` en Railway y
Whitenoise los sirve desde allí con las URLs `/static/...`
