from django.urls import path
from appoitments import views

urlpatterns = [
    path('appoitmentsList', views.appoitmentsList, name='appoitmentsList'),
    path('addAppoitment', views.addAppoitment, name='addAppoitment'),
    path('appoitmentList/<int:id>', views.info, name='info'),
    path('appoitmentList/Atualizar/<int:id>', views.updateAppoitment, name='updateAppoitment')
    
]
