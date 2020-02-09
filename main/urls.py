from main import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('thank_you/', views.thank_you, name='thank_you'),
]
