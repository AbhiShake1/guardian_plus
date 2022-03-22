from . import views
from django.urls import path

urlpatterns = [
    path('signin/', views.login),
    path('current_user/', views.current_user),
    path('signout/', views.signout),
]
