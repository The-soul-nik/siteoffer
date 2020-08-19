from django.urls import path
from .views import *
from .import views

app_name = "blog"


urlpatterns = [
    path('', views.posts_list, name="posts_list_url"),
    path('post/<str:slug>/', PostDetail.as_view(), name="post_detail_url"),
    path('tags/', views.tags_list, name="tags_list_url"),
    path('tag/create', TagCreate.as_view(), name="tag_create_url"),
    path('taga/<str:slug2>/',  TagDetail.as_view(), name="tags_detail_url"),

]
