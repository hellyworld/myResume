from django.urls import path
from curriculum import views

urlpatterns = [
    path('', views.resume, name='resume'),
]
