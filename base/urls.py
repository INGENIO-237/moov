from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demadeDevis/', views.devis, name='devis'),
    
]

