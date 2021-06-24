from django.urls import path
from . import views

app_name = 'path'
urlpatterns = [
    path('', views.index, name='index'),
    path('connectNode/', views.connect_node, name='connect_node'),
]
