from django.urls import path

from . import views

urlpatterns = [
    path('get_child_progress/', views.get_child_progress),
]
