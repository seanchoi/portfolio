from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('nameFormat/<str:name>/', views.nameCheck),
    path('emailCheck/', views.emailCheck),
    path('userIdCheck/', views.userIdCheck),
    path('passwordCheck/', views.passwordCheck),
    path('loginIdCheck/', views.loginIdCheck),
    path('login/', views.login),
    path('logout/', views.logout),
    path('<str:user_id>/', views.dashboard),
    path('<str:user_id>/profile_pic/', views.profilePic),
    path('<str:user_id>/profile_pic_delete/', views.profilePicDelete),
]