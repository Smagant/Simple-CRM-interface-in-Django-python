from django.urls import path
from . import views

urlpatterns = [
    #Lien vers la page de connection de l'application
    path('login/', views.loginPage, name='login'),
    #Lien vers la page de déconexion de l'application
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('clientsbase/', views.clientsBasepage, name='clientsbase'),
    path('client/', views.clientPage, name='client-page'),
    path('videobase/', views.videoBasepage, name='videobase'),
    path('video/', views.videoBasepage, name='video-page'),

    path('customer/<str:pk>/', views.customer, name='customer'),
    path('create_order/<str:pk>/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),
]