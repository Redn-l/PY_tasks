from django.urls import path
from .views import register
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('register/', register, name='register'),
]

urlpatterns += router.urls
