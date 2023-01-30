from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='HOME'),
    path('fun', views.fun, name='FUN'),
    path('lowest', views.lowest, name='LOWEST'),
    path('encoder', views.encoder, name='ENCODER'),
    path('path', views.path, name='PATH'),
]
