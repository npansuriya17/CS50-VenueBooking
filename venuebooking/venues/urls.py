from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('post/<str:var>',views.post, name='post'),
    path('find/<str:var>',views.find, name='find'),
    path('view/<int:id', views.find, name='view')
]