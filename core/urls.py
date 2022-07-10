from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('djoser.urls')),
    path('api/v1/', include('djoser.urls.jwt')),
    path('api/v1/empresa/',include("apps.Empresa.urls",namespace="empresa")),
]