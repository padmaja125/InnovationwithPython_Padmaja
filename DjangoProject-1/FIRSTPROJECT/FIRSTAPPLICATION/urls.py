from django.urls import path

from . import views

urlpatterns = [
    path('h/ts/', views.test, name='test'),
    path('tr/', views.trial, name='trial'),
    path('h/', views.html, name = 'html'),
    path('id/', views.Idview, name = 'Id'),
    path('name/', views.Nameview, name = 'Name'),
    path('address/', views.Addressview, name = 'Address'),
    path('id/ts/', views.test, name='test'),
    path('name/ts/', views.test, name='test'),
    path('address/ts/', views.test, name='test'),
]