from django.urls import path
from .views import upload_image, image_list, delete_image, tag_list

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
    path('tags/', tag_list, name='tag_list'),
    path('', image_list, name='image_list'),
     path('delete_image/<int:image_id>/', delete_image, name='delete_image'),
]
