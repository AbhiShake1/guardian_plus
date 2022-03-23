from . import views
from django.urls import path

urlpatterns = [
    path('get_all/', views.get_assessments),
]
