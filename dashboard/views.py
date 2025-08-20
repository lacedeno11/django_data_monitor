from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import requests
from django.conf import settings
import logging

# Configurar logging
logger = logging.getLogger(__name__)

@login_required
def index(request):
    """Vista principal del dashboard con contexto dinámico"""
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
    
    data = {
        'title': "Landing Page' Dashboard",
        'total_responses': total_responses,
    }
    return render(request, 'dashboard/index.html', data)
