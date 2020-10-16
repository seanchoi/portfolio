from django.urls import path
from . import views

urlpatterns = [
    path('multiple_img/', views.multipleImg),
    path('img_upload/', views.imageUpload),
    path('clear_img/', views.clear_images),
    path('new_memo/', views.newMemo),
    path('memo_delete/<int:memo_id>/', views.deleteMemo)
]