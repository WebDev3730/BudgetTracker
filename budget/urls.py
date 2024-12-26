from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import home, AddTransaction, EditTransaction, logout_user

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', logout_user, name='logout'),
    path('add_transaction/', views.AddTransaction, name="add_transaction"),
    path('register/', views.register, name='register'),
    path('edit_transaction/<int:pk>', views.EditTransaction, name='edit_transaction'),
    path('delete_transaction/<int:pk>', views.DeleteTransaction, name='delete_transaction'),
    
]