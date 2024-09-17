from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_item/', views.add_item, name='add_item'),
    re_path(r'^(?!users)(?P<slug1>[-\w]+)/$', views.index, name='slug1'),
    re_path(r'^(?!users)(?P<slug1>[-\w]+)/(?P<slug2>[-\w]+)/$', views.index, name='slug2'),
    re_path(r'^(?!users)(?P<slug1>[-\w]+)/(?P<slug2>[-\w]+)/(?P<slug3>[-\w]+)/$', views.index, name='slug3'),
    re_path(r'^(?!users)(?P<slug1>[-\w]+)/(?P<slug2>[-\w]+)/(?P<slug3>[-\w]+)/(?P<slug4>[-\w]+)/$', views.index, name='slug4'),
]