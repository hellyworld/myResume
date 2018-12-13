from django.urls import path
from curriculum import views

urlpatterns = [
    path('', views.home, name='home'),
]
