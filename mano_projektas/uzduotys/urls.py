from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('uzduotis/sukurti/', views.task_create, name='task_create'),
    path('uzduotis/<int:pk>/redaguoti/', views.task_edit, name='task_edit'),
    path('uzduotis/<int:pk>/istrinti/', views.task_delete, name='task_delete'),
    path('uzduotis/<int:pk>/keitimas/', views.task_toggle_complete, name='task_toggle_complete'),
]