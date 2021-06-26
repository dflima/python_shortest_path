from django.urls import path
from . import views

app_name = 'path'
urlpatterns = [
    path('path/', views.PathList.as_view(), name='index'),
    path('connectNode/', views.ConnectNode.as_view(), name='connect_node'),
]
