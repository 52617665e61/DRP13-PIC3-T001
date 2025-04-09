from django.urls import path
from services import views

urlpatterns = [
    path('servicesList', views.servicesList, name='servicesList'),
    path('addService', views.addService, name='addService'),
    path('manager/service', views.manager, name='managerService'),
    path('updateService/<int:id>', views.updateService, name='updateService'),
    path('delService/<int:id>', views.delService, name='delService')
]
