from django.urls import path
from . import views

urlpatterns = [
    path('c/', views.create, name='create'),
    path('list/', views.table_list, name='list'),
    path('view/<int:pk>', views.table_view, name='table_view'),
    path('new/', views.table_create, name='table_new'),
    path('edit/<int:pk>', views.table_update, name='table_edit'),
    path('delete/<int:pk>', views.table_delete, name='table_delete'),
]