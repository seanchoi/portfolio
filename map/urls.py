from django.urls import path
from . import views

urlpatterns = [
    path('google/', views.Map),
    path('data-delete/', views.dataDelete)
]