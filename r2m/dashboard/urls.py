from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clientsbase/', views.clientsBasePage, name='clientsbase'),
    path('client/<str:pk>/', views.clientPage, name='client'),
    path('videobase/', views.videoBasePage, name='videobase'),
    path('video/<str:pk>/', views.videoPage, name='video'),

    #path('create_order/<str:pk>/', views.createOrder, name='create_order'),
    #path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    #path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),
]