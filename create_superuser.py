#!/usr/bin/env python
"""
Script para crear superusuario y grupos en Railway
Ejecutar: python create_superuser.py
"""
import os
import django
import sys

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_analytics_server.settings')
django.setup()

from django.contrib.auth.models import User, Group

def create_superuser_and_groups():
    """Crear superusuario y grupos necesarios"""
    
    # Crear grupos
    dashboard_group, created = Group.objects.get_or_create(name='Dashboard Users')
    restricted_group, created = Group.objects.get_or_create(name='Restricted Users')
    
    print("✅ Grupos creados/verificados")
    
    # Crear superusuario si no existe
    username = 'admin'
    email = 'admin@example.com'
    password = 'admin123'
    
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f"✅ Superusuario '{username}' creado")
    else:
        print(f"ℹ️  Superusuario '{username}' ya existe")
    
    # Crear usuario normal para dashboard
    normal_username = 'usuario'
    normal_email = 'usuario@example.com'
    normal_password = 'password123'
    
    if not User.objects.filter(username=normal_username).exists():
        normal_user = User.objects.create_user(normal_username, normal_email, normal_password)
        normal_user.groups.add(dashboard_group)
        print(f"✅ Usuario normal '{normal_username}' creado y añadido al grupo Dashboard Users")
    else:
        print(f"ℹ️  Usuario '{normal_username}' ya existe")
    
    print("\n🎉 Setup completado!")
    print(f"   Admin: {username} / {password}")
    print(f"   Usuario: {normal_username} / {normal_password}")

if __name__ == '__main__':
    create_superuser_and_groups()
