from django.urls import path
from appoitments import views

urlpatterns = [
    path('appoitmentsList', views.appoitmentsList),
    path('addAppoitment', views.addAppoitment, name='addAppoitment'),
    
]
