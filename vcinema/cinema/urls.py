from django.urls import path
from . import views

app_name = 'cinema'
urlpatterns = [
    path('', views.index, name='main'),
    path('detail/<str:pk>/', views.detail, name='detail'),
    path('register/', views.register, name='register'),
    path('authorize/', views.authorize, name='authorize'),
    path('logout/', views.logout_view, name='logout')
]
