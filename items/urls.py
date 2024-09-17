from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_item/', views.add_item, name='add_item'),
    path('<slug:slug1>/', views.index, name='slug1'),
    path('<slug:slug1>/<slug:slug2>/', views.index, name='slug2'),
    path('<slug:slug1>/<slug:slug2>/<slug:slug3>/', views.index, name='slug3'),
    path('<slug:slug1>/<slug:slug2>/<slug:slug3>/<slug:slug4>/', views.index, name='slug4'),
]