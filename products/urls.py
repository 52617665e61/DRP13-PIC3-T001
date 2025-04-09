from django.urls import path
from products import views

urlpatterns = [
    path('productsList', views.productsList, name='productsList'),
    path('addProduct', views.addProduct, name='addProduct'),
    path('manager/product', views.manager, name='managerProduct'),
    path('updateProduct/<int:id>', views.updateProduct, name='updateProduct'),
    path('delProduct/<int:id>', views.delProduct, name='delProduct'),
    
]
