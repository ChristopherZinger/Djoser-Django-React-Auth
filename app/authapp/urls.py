from django.urls import path, include
from . import views


urlpatterns = [
    path('index/', views.index, name="index"),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken'))
]
