from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.home),
    path('homeAdmin', views.homeAdmin, name='homeAdmin'),
    path('home', views.homeUser, name='homeUser'),
]
