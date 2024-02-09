# blog/urls.py

from django.urls import path
from .views import category_list, post_list_by_category, post_detail

app_name = 'blog' 

urlpatterns = [
    path('categories/', category_list, name='categories'),
    path('category/<int:category_id>/', post_list_by_category, name='post_list_by_category'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
]
