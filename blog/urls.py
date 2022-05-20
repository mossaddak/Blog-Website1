from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('blogs', views.blogs, name="blogs"),
    path('category_blogs/<str:slug>/', views.category_blogs, name="category_blogs"),
    path('tag_blogs/<str:slug>/', views.tag_blogs, name="tag_blogs"),
    path('blog/<str:slug>/', views.blog_details, name="blog_details"),
    path('add_reply/<int:blog_id>/<int:comment_id>/', views.add_reply, name="add_reply"),
    path('like_blog/<int:pk>/', views.like_blog, name = 'like_blog'),
    path('search_blogs/', views.search_blogs, name="search_blogs"),
    path('my_blogs/', views.my_blogs, name="my_blogs"),
    path('add_blog/', views.add_blog, name="add_blog"),
    path('update_blog/<str:slug>/', views.update_blog, name="update_blog") 
]