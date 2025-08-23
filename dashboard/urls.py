from django.urls import path

from .views import index, emergency_dashboard

urlpatterns = [
    path('', index, name='dashboard'),
    path('emergency/', emergency_dashboard, name='emergency_dashboard'),
]