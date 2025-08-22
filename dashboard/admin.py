from django.contrib import admin
from .models import Post, UserStats, DashboardMetrics, APILog, DashboardModel

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('api_id', 'user_id', 'title', 'created_at')
    list_filter = ('user_id', 'created_at')
    search_fields = ('title', 'body')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

@admin.register(UserStats)
class UserStatsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'post_count', 'avg_post_length', 'last_updated')
    list_filter = ('last_updated',)
    search_fields = ('username',)
    readonly_fields = ('last_updated',)
    ordering = ('-post_count',)

@admin.register(DashboardMetrics)
class DashboardMetricsAdmin(admin.ModelAdmin):
    list_display = ('date', 'total_posts', 'active_users', 'avg_posts_per_user', 'api_response_time')
    list_filter = ('date',)
    ordering = ('-date',)
    readonly_fields = ('created_at',)

@admin.register(APILog)
class APILogAdmin(admin.ModelAdmin):
    list_display = ('endpoint', 'status_code', 'response_time', 'timestamp')
    list_filter = ('status_code', 'timestamp')
    search_fields = ('endpoint', 'error_message')
    readonly_fields = ('timestamp',)
    ordering = ('-timestamp',)

@admin.register(DashboardModel)
class DashboardModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
