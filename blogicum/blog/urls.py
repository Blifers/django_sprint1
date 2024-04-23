from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='blog_index'),
    path('<int:id>/', views.post_detail, name='blog_post_detail'),
    path('<slug:category_slug>/', views.category_posts,
         name='blog_category_posts'),
]
