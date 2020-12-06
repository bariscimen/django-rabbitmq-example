from django.urls import path

from ordersite import views

urlpatterns = [
    path('', views.index, name='index'),
]
