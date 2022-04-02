from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
        path('get_children/', views.get_children),
        path('get_child_subjects/', views.get_child_subjects),
        path('get_child_progress/', views.get_child_progress),
]
