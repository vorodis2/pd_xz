"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')) cdvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
"""
from django.contrib import admin
from django.urls import path, include
from djoser.views import UserViewSet
from rest_framework.authtoken.views import obtain_auth_token

from api import settings
from django.contrib.auth.views import LogoutView, LoginView  # , LoginView

FAVICON = 'favicon.ico'


urlpatterns = [

    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    # path('auth/', include('accounts.urls')),
    path('auth/', UserViewSet),


    path('admin/', admin.site.urls),
    path('social_auth/', include('social_django.urls', namespace='social')),

    path('social_auth/login/', LoginView.as_view(), {'next_page': settings.LOGIN_REDIRECT_URL}, name='logout'),
    path('social_auth/logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),



    path('api/v1/group/', include('apps.group.urls')),
]