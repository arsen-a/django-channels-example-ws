from django.urls import path
from .views import PostsView

urlpatterns = [
    path('posts/', PostsView.as_view())
]
