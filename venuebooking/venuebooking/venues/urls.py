from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('post/<str:var>',views.post, name='post'),
    path('find/<str:var>',views.find, name='find'),
    path('view/<int:id>', views.view, name='view'),


    # API Routes
    path("lists/<str:var>", views.lists, name="lists"),
    path("shows/<int:id>", views.list_item, name="list_item"),
    path("artists/<int:id>", views.list_item, name="list_item"),
    path("venues/<int:id>", views.list_item, name="list_item"),
]