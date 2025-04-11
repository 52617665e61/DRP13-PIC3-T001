from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('tasks.urls')),
    path('', include('services.urls')),
    path('', include('products.urls')),
    path('', include('appoitments.urls')),
    path('', include('users.urls'))
]
