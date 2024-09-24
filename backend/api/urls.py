from django.urls import path

from . import views

urlpatterns = [
    path( 'api-token-auth/', views.obtain_jwt_token),
    path('', views.api_home),
    path('api/', views.api_home),
]