from django.urls import path

from . import views

urlpatterns = [
    path('airline/', views.AirlineList.as_view()),
    path('aircraft/', views.AircraftCreate.as_view()),
    path('airline/<int:pk>', views.AirlineDetail.as_view()),
    path('aircraft/<int:pk>', views.AircraftDetail.as_view()),
]