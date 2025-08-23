from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
import requests
from django.conf import settings
import logging

# Configurar logging
logger = logging.getLogger(__name__)

def is_dashboard_user(user):
    """Verifica si el usuario tiene acceso al dashboard"""
    if user.is_superuser:
        return True
    return user.groups.filter(name='Dashboard Users').exists()

def is_restricted_user(user):
    """Verifica si el usuario está restringido (para pruebas de 403)"""
    return user.groups.filter(name='Restricted Users').exists()

@login_required
def index(request):
    """Vista principal del dashboard con control de acceso"""
    
    # Si es un usuario restringido, mostrar error 403
    if is_restricted_user(request.user):
        raise PermissionDenied("No tienes permisos para acceder a esta sección")
    
    # Verificar si tiene acceso al dashboard
    if not is_dashboard_user(request.user) and not request.user.is_superuser:
        raise PermissionDenied("Acceso denegado al dashboard")
    
    # Valores por defecto en caso de error de API
    total_responses = 0
    
    try:
        # Solicitud GET a JSONPlaceholder API
        response = requests.get(settings.API_URL, timeout=10)
        response.raise_for_status()  # Lanza excepción para códigos HTTP de error
        posts = response.json()
        
        # Calcular número total de respuestas
        total_responses = len(posts)
        logger.info(f"API llamada exitosa: {total_responses} posts obtenidos")
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Error al conectar con la API: {e}")
        total_responses = 0  # Valor por defecto
    except ValueError as e:
        logger.error(f"Error al procesar JSON de la API: {e}")
        total_responses = 0
    except Exception as e:
        logger.error(f"Error inesperado: {e}")
        total_responses = 0
    
    # Información adicional para el dashboard
    user_info = {
        'username': request.user.username,
        'is_superuser': request.user.is_superuser,
        'is_staff': request.user.is_staff,
        'groups': [group.name for group in request.user.groups.all()],
    }
    
    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,
        'user_info': user_info,
    }
    return render(request, 'dashboard/index.html', data)

@login_required 
@user_passes_test(is_dashboard_user)
def admin_view(request):
    """Vista exclusiva para administradores y usuarios de dashboard"""
    users = User.objects.all()
    return render(request, 'dashboard/admin.html', {'users': users})

@login_required
def restricted_test(request):
    """Vista para probar el error 403 con usuarios restringidos"""
    if is_restricted_user(request.user):
        raise PermissionDenied("Usuario restringido - Error 403 de prueba")
    
    return render(request, 'dashboard/test.html', {
        'message': 'Solo usuarios no restringidos pueden ver esto'
    })
