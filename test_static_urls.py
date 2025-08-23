#!/usr/bin/env python
"""
Script para probar las URLs de archivos estáticos en Django
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_analytics_server.settings')

try:
    django.setup()
    from django.conf import settings
    from django.contrib.staticfiles import finders
    from django.templatetags.static import static
    
    print("🔍 DIAGNÓSTICO DE ARCHIVOS ESTÁTICOS")
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
    
    print("\n📁 ARCHIVOS CRÍTICOS:")
    print("-" * 30)
    
    critical_files = [
        'css/tailwind.output.css',
        'js/init-alpine.js',
        'js/charts-lines.js',
        'img/dashboard.png'
    ]
    
    for file_path in critical_files:
        try:
            # Buscar archivo
            found_file = finders.find(file_path)
            # Generar URL estática
            static_url = static(file_path)
            
            status = "✅ ENCONTRADO" if found_file else "❌ NO ENCONTRADO"
            print(f"{file_path}: {status}")
            if found_file:
                print(f"  📍 Ubicación: {found_file}")
            print(f"  🔗 URL: {static_url}")
            print()
        except Exception as e:
            print(f"❌ Error con {file_path}: {e}")
    
except Exception as e:
    print(f"❌ Error al configurar Django: {e}")
    sys.exit(1)
