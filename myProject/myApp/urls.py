from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("category", views.category, name="category"),
    path("posts", views.posts, name="posts"),
]