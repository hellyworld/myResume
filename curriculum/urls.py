from django.urls import path
from curriculum import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume', views.resume, name='resume'),
]
