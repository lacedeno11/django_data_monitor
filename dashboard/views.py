from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
import requests
from django.conf import settings
import logging

# Configurar logging
logger = logging.getLogger(__name__)

@login_required
@permission_required('dashboard.index_viewer', raise_exception=True)
def index(request):
    """Vista principal del dashboard con datos de django_api_suite y respaldo"""
    # Valores por defecto en caso de error de API
    demo_users_count = 0
    landing_data_count = 0
    api_status = "Verificando..."
    api_source = "django_api_suite"
    
    try:
        # 1. Intentar conectar con Demo REST API
        demo_response = requests.get(settings.API_URLS['demo_users'], timeout=5)
        if demo_response.status_code == 200:
            demo_data = demo_response.json()
            if isinstance(demo_data, dict) and 'data' in demo_data:
                demo_users_count = demo_data.get('count', len(demo_data['data']))
            elif isinstance(demo_data, list):
                demo_users_count = len(demo_data)
            logger.info(f"Demo API exitosa: {demo_users_count} usuarios activos")
        else:
            raise requests.exceptions.RequestException(f"Status code: {demo_response.status_code}")
            
    except requests.exceptions.RequestException as e:
        logger.warning(f"Error con Demo API, usando respaldo: {e}")
        # Usar API de respaldo (JSONPlaceholder)
        try:
            backup_response = requests.get(settings.API_URLS['backup_api'], timeout=5)
            if backup_response.status_code == 200:
                backup_data = backup_response.json()
                demo_users_count = len(backup_data)
                api_source = "JSONPlaceholder (respaldo)"
                logger.info(f"API de respaldo exitosa: {demo_users_count} usuarios")
        except Exception as backup_error:
            logger.error(f"Error también en API de respaldo: {backup_error}")
    
    try:
        # 2. Intentar Landing API (Firebase)
        landing_response = requests.get(settings.API_URLS['landing_data'], timeout=5)
        if landing_response.status_code == 200:
            landing_data = landing_response.json()
            if isinstance(landing_data, dict):
                landing_data_count = len(landing_data) if landing_data else 0
            elif isinstance(landing_data, list):
                landing_data_count = len(landing_data)
            logger.info(f"Landing API exitosa: {landing_data_count} registros")
        else:
            logger.warning(f"Landing API retornó código {landing_response.status_code}")
            
    except requests.exceptions.RequestException as e:
        logger.warning(f"Error con Landing API: {e}")
        # Simular algunos datos para la demo
        landing_data_count = 5  # Dato simulado
    
    # Determinar estado general de APIs
    if demo_users_count > 0:
        api_status = "Conectado"
    else:
        api_status = "Desconectado"
    
    # Datos del contexto para el template
    data = {
        'title': "Django API Suite Dashboard",
        'demo_users_count': demo_users_count,
        'landing_data_count': landing_data_count,
        'total_records': demo_users_count + landing_data_count,
        'api_status': api_status,
        'api_source': api_source,
        'api_base_url': settings.API_BASE_URL,
    }
    
    return render(request, 'dashboard/index.html', data)
