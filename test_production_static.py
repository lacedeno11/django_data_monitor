#!/usr/bin/env python
"""
Script para probar configuración de producción de archivos estáticos
"""
import os
import sys

# Simular entorno de producción
os.environ['MYSQLDATABASE'] = 'test'
os.environ['DEBUG'] = 'False'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_analytics_server.settings')

try:
    import django
    from django.conf import settings
    
    # Modificar configuración de BD para evitar errores
    settings.DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }
    
    django.setup()
    
    from django.contrib.staticfiles import finders
    from django.templatetags.static import static
    
    print("🚀 DIAGNÓSTICO MODO PRODUCCIÓN")
    print("=" * 50)
    
    print(f"DEBUG: {settings.DEBUG}")
    print(f"STATIC_URL: {settings.STATIC_URL}")
    print(f"STATIC_ROOT: {settings.STATIC_ROOT}")
    print(f"STATICFILES_DIRS: {settings.STATICFILES_DIRS}")
    print(f"STATICFILES_STORAGE: {settings.STATICFILES_STORAGE}")
    
    if hasattr(settings, 'WHITENOISE_USE_FINDERS'):
        print(f"WHITENOISE_USE_FINDERS: {settings.WHITENOISE_USE_FINDERS}")
    if hasattr(settings, 'WHITENOISE_AUTOREFRESH'):
        print(f"WHITENOISE_AUTOREFRESH: {settings.WHITENOISE_AUTOREFRESH}")
    if hasattr(settings, 'WHITENOISE_MAX_AGE'):
        print(f"WHITENOISE_MAX_AGE: {settings.WHITENOISE_MAX_AGE}")
    
    print("\n📁 ARCHIVOS EN STATICFILES:")
    print("-" * 30)
    
    critical_files = [
        'css/tailwind.output.css',
        'js/init-alpine.js', 
        'js/charts-lines.js',
        'img/dashboard.png'
    ]
    
    for file_path in critical_files:
        try:
            # En producción, verificar en STATIC_ROOT
            full_path = os.path.join(settings.STATIC_ROOT, file_path)
            exists = os.path.exists(full_path)
            static_url = static(file_path)
            
            status = "✅ EXISTE" if exists else "❌ NO EXISTE"
            print(f"{file_path}: {status}")
            if exists:
                print(f"  📍 Ubicación: {full_path}")
            print(f"  🔗 URL: {static_url}")
            print()
        except Exception as e:
            print(f"❌ Error con {file_path}: {e}")
    
    print("\n🔧 CONFIGURACIÓN WHITENOISE:")
    print("-" * 30)
    whitenoise_attrs = [attr for attr in dir(settings) if attr.startswith('WHITENOISE_')]
    for attr in whitenoise_attrs:
        print(f"{attr}: {getattr(settings, attr)}")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
