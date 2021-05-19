from rest_framework.generics import ListCreateAPIView
from .models import Post
from .serializers import PostSerializer


class PostsView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
