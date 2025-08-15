from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Count, Avg, Max, Min
from .models import Post, UserStats, DashboardMetrics, APILog
import requests
import time
import math
from datetime import datetime, timedelta

def sync_api_data():
    """
    Sincroniza datos de la API con la base de datos local
    """
    try:
        start_time = time.time()
        response = requests.get(settings.API_URL, timeout=10)
        response_time = time.time() - start_time
        
        # Log API call
        api_log = APILog.objects.create(
            endpoint=settings.API_URL,
            status_code=response.status_code,
            response_time=response_time,
            response_size=len(response.content)
        )
        
        if response.status_code == 200:
            posts_data = response.json()
            
            # Sync posts to database
            for post_data in posts_data:
                post, created = Post.objects.get_or_create(
                    api_id=post_data['id'],
                    defaults={
                        'user_id': post_data['userId'],
                        'title': post_data['title'],
                        'body': post_data['body']
                    }
                )
            
            # Update user statistics
            user_stats = {}
            for post in Post.objects.all():
                if post.user_id not in user_stats:
                    user_stats[post.user_id] = {
                        'count': 0,
                        'total_length': 0,
                        'posts': []
                    }
                user_stats[post.user_id]['count'] += 1
                user_stats[post.user_id]['total_length'] += len(post.body)
                user_stats[post.user_id]['posts'].append(post)
            
            # Save user statistics
            for user_id, stats in user_stats.items():
                user_stat, created = UserStats.objects.get_or_create(
                    user_id=user_id,
                    defaults={'username': f'User {user_id}'}
                )
                user_stat.post_count = stats['count']
                user_stat.avg_post_length = stats['total_length'] / stats['count']
                user_stat.first_post_date = min(post.created_at for post in stats['posts'])
                user_stat.last_post_date = max(post.created_at for post in stats['posts'])
                user_stat.save()
            
            # Update daily metrics
            today = timezone.now().date()
            metrics, created = DashboardMetrics.objects.get_or_create(
                date=today,
                defaults={
                    'total_posts': Post.objects.count(),
                    'active_users': UserStats.objects.count(),
                    'avg_posts_per_user': Post.objects.count() / UserStats.objects.count() if UserStats.objects.count() > 0 else 0,
                    'api_response_time': response_time * 1000  # Convert to ms
                }
            )
            
            return True, len(posts_data)
            
    except Exception as e:
        # Log error
        APILog.objects.create(
            endpoint=settings.API_URL,
            status_code=0,
            response_time=0,
            response_size=0,
            error_message=str(e)
        )
        return False, str(e)

def generate_function_data():
    """
    Genera datos para gráficos tipo función matemática
    """
    # Función seno para posts por día
    days = list(range(30))  # Últimos 30 días
    sine_data = []
    for day in days:
        # Función seno con amplitud y offset
        value = 50 + 30 * math.sin(day * math.pi / 15)  # Período de 30 días
        sine_data.append({
            'day': day,
            'value': round(value, 1),
            'label': f'Day {day + 1}'
        })
    
    # Función exponencial para crecimiento de usuarios
    exponential_data = []
    for day in days:
        # Función exponencial suavizada
        value = 10 * (1 + math.exp(day / 20) / 100)
        exponential_data.append({
            'day': day,
            'value': round(value, 1),
            'label': f'Day {day + 1}'
        })
    
    # Función logarítmica para engagement
    logarithmic_data = []
    for day in days:
        # Función logarítmica
        value = 20 * math.log(day + 1) + 10
        logarithmic_data.append({
            'day': day,
            'value': round(value, 1),
            'label': f'Day {day + 1}'
        })
    
    # Función cuadrática para performance
    quadratic_data = []
    for day in days:
        # Función cuadrática invertida (parábola hacia abajo)
        value = 100 - (day - 15) ** 2 / 10
        quadratic_data.append({
            'day': day,
            'value': max(0, round(value, 1)),
            'label': f'Day {day + 1}'
        })
    
    return {
        'sine_function': sine_data,
        'exponential_function': exponential_data,
        'logarithmic_function': logarithmic_data,
        'quadratic_function': quadratic_data
    }

@login_required
def index(request):
    # Sync data from API
    sync_success, sync_result = sync_api_data()
    
    # Get data from database
    posts = Post.objects.all()[:10]  # Latest 10 posts
    user_stats = UserStats.objects.all()[:10]  # Top 10 users
    total_posts = Post.objects.count()
    total_users = UserStats.objects.count()
    
    # Generate function-based chart data
    function_data = generate_function_data()
    
    # Create chart data for users
    chart_data = []
    for user_stat in user_stats[:5]:  # Top 5 users
        percentage = (user_stat.post_count / total_posts * 100) if total_posts > 0 else 0
        chart_data.append({
            'user': user_stat.username,
            'posts': user_stat.post_count,
            'percentage': round(percentage, 1)
        })
    
    # Status indicators
    avg_posts_per_user = total_posts / total_users if total_users > 0 else 0
    latest_api_log = APILog.objects.first()
    api_status = 'Online' if sync_success else 'Error'
    api_color = 'green' if sync_success else 'red'
    
    status_indicators = [
        {
            'title': 'Total Posts',
            'value': total_posts,
            'icon': 'posts',
            'color': 'blue',
            'trend': 'up'
        },
        {
            'title': 'Active Users',
            'value': total_users,
            'icon': 'users',
            'color': 'green',
            'trend': 'up'
        },
        {
            'title': 'Avg Posts/User',
            'value': round(avg_posts_per_user, 1),
            'icon': 'average',
            'color': 'purple',
            'trend': 'stable'
        },
        {
            'title': 'API Status',
            'value': api_status,
            'icon': 'status',
            'color': api_color,
            'trend': 'up' if sync_success else 'down'
        }
    ]
    
    # Convert user_stats to dict for template compatibility
    user_stats_dict = {stat.user_id: stat.post_count for stat in user_stats}
    
    # Recent metrics for trends
    recent_metrics = DashboardMetrics.objects.all()[:7]  # Last 7 days
    
    context = {
        'title': 'Analytics Dashboard',
        'total_responses': total_posts,
        'posts': posts,
        'user_stats': user_stats_dict,
        'user_stats_objects': user_stats,
        'chart_data': chart_data,
        'status_indicators': status_indicators,
        'function_data': function_data,
        'recent_metrics': recent_metrics,
        'sync_success': sync_success,
        'sync_result': sync_result,
        'latest_api_log': latest_api_log
    }
    
    return render(request, 'dashboard/index.html', context)
