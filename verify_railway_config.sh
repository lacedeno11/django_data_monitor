#!/bin/bash
# Script de verificación final para Railway deployment

echo "🚀 SIMULANDO DEPLOY EN RAILWAY"
echo "================================"

# 1. Simular variables de entorno de Railway
export MYSQLDATABASE="railway_db"
export MYSQLUSER="root"
export MYSQLPASSWORD="password"
export MYSQLHOST="localhost"
export MYSQLPORT="3306"
export DEBUG="False"

echo "✅ Variables de entorno configuradas"

# 2. Ejecutar collectstatic como en Railway
echo "📦 Ejecutando collectstatic..."
python manage.py collectstatic --noinput --clear

if [ $? -eq 0 ]; then
    echo "✅ collectstatic exitoso"
else
    echo "❌ Error en collectstatic"
    exit 1
fi

# 3. Verificar archivos críticos
echo "🔍 Verificando archivos críticos..."
critical_files=(
    "staticfiles/css/tailwind.output.css"
    "staticfiles/js/init-alpine.js"
    "staticfiles/js/charts-lines.js"
    "staticfiles/img/dashboard.png"
)

for file in "${critical_files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file existe"
    else
        echo "❌ $file NO ENCONTRADO"
    fi
done

# 4. Verificar configuración de Django
echo "⚙️  Verificando configuración..."
python -c "
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_analytics_server.settings')
from django.conf import settings
print(f'DEBUG: {settings.DEBUG}')
print(f'STATICFILES_STORAGE: {settings.STATICFILES_STORAGE}')
print(f'STATIC_URL: {settings.STATIC_URL}')
print(f'STATIC_ROOT: {settings.STATIC_ROOT}')
"

echo "🎉 VERIFICACIÓN COMPLETA"
echo "Si todos los elementos muestran ✅, la configuración está lista para Railway"
