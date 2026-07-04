"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import ApplicationViewSet, JobViewSet, UserViewSet

# 1. Create a SINGLE router instance
router = DefaultRouter()

# 2. Register ALL your ViewSets to this one single router
router.register(r'jobs', JobViewSet, basename='job')
router.register(r'users', UserViewSet, basename='user')
router.register(r'applications', ApplicationViewSet, basename='application')

# 3. Define your SINGLE urlpatterns list
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This automatically handles all generated endpoints for jobs, users, and applications!
    path('api/', include(router.urls)),
]