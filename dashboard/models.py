from django.db import models
from django.utils import timezone

class Post(models.Model):
    """
    Modelo para almacenar posts de JSONPlaceholder API
    """
    api_id = models.IntegerField(unique=True, help_text="ID del post en la API")
    user_id = models.IntegerField(help_text="ID del usuario que creó el post")
    title = models.CharField(max_length=255, help_text="Título del post")
    body = models.TextField(help_text="Contenido del post")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Fecha de creación en BD")
    updated_at = models.DateTimeField(auto_now=True, help_text="Fecha de última actualización")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
    def __str__(self):
        return f"Post {self.api_id}: {self.title[:50]}..."

class UserStats(models.Model):
    """
    Modelo para estadísticas de usuarios
    """
    user_id = models.IntegerField(unique=True, help_text="ID del usuario")
    username = models.CharField(max_length=100, blank=True, help_text="Nombre del usuario")
    post_count = models.IntegerField(default=0, help_text="Número total de posts")
    avg_post_length = models.FloatField(default=0.0, help_text="Promedio de caracteres por post")
    first_post_date = models.DateTimeField(null=True, blank=True, help_text="Fecha del primer post")
    last_post_date = models.DateTimeField(null=True, blank=True, help_text="Fecha del último post")
    last_updated = models.DateTimeField(auto_now=True, help_text="Última actualización de stats")
    
    class Meta:
        ordering = ['-post_count']
        verbose_name = "User Statistic"
        verbose_name_plural = "User Statistics"
    
    def __str__(self):
        return f"User {self.user_id}: {self.post_count} posts"

class DashboardMetrics(models.Model):
    """
    Modelo para métricas del dashboard por fecha
    """
    date = models.DateField(unique=True, help_text="Fecha de las métricas")
    total_posts = models.IntegerField(default=0, help_text="Total de posts ese día")
    active_users = models.IntegerField(default=0, help_text="Usuarios activos ese día")
    avg_posts_per_user = models.FloatField(default=0.0, help_text="Promedio posts por usuario")
    api_response_time = models.FloatField(default=0.0, help_text="Tiempo de respuesta API en ms")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
        verbose_name = "Dashboard Metric"
        verbose_name_plural = "Dashboard Metrics"
    
    def __str__(self):
        return f"Metrics {self.date}: {self.total_posts} posts"

class APILog(models.Model):
    """
    Modelo para logs de llamadas a la API
    """
    endpoint = models.CharField(max_length=255, help_text="Endpoint de la API")
    status_code = models.IntegerField(help_text="Código de respuesta HTTP")
    response_time = models.FloatField(help_text="Tiempo de respuesta en segundos")
    response_size = models.IntegerField(help_text="Tamaño de respuesta en bytes")
    timestamp = models.DateTimeField(auto_now_add=True, help_text="Timestamp de la llamada")
    error_message = models.TextField(blank=True, help_text="Mensaje de error si aplica")
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = "API Log"
        verbose_name_plural = "API Logs"
    
    def __str__(self):
        return f"API Call {self.endpoint} - {self.status_code} ({self.timestamp})"

class DashboardModel(models.Model):
    """
    Modelo para permisos personalizados del dashboard
    """
    name = models.CharField(max_length=100, help_text="Nombre del dashboard")
    description = models.TextField(blank=True, help_text="Descripción del dashboard")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        permissions = [
            ("index_viewer", "Can show to index view (function-based)"),
        ]
        verbose_name = "Dashboard Model"
        verbose_name_plural = "Dashboard Models"
    
    def __str__(self):
        return self.name
