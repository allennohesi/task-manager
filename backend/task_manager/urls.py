"""
URL configuration for task_manager project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('api/docs/', TemplateView.as_view(template_name='api_docs.html'), name='api-docs'),
]

