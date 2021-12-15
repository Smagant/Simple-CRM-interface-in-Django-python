from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clientsbase/', views.clientsBasePage, name='clientsbase'),
    path('client/<str:pk>/', views.clientPage, name='client'),
    path('videobase/', views.videoBasePage, name='videobase'),
    path('video/<str:pk>/', views.videoPage, name='video'),

    path('create_video/<str:pk>/', views.createVideo, name='create_video'),
    path('update_video/<str:pk>/', views.updateVideo, name='update_video'),
    path('delete_video/<str:pk>/', views.deleteVideo, name='delete_video'),

    path('create_client/', views.createClient, name='create_client'),
    path('update_client/<str:pk>/', views.updateClient, name='update_client'),
    path('delete_client/<str:pk>/', views.deleteClient, name='delete_client')
]