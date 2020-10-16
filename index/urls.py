from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dm/', views.DM),
    path('dm_check/', views.checkDM),
    path('dm_delete/<int:dm_id>/', views.deleteDM)
]