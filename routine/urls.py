from django.urls import path
from . import views

urlpatterns = [
        path('get_all/', views.get_all_routine),
]
