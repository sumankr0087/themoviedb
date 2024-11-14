from rest_framework import generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Prefetch
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.exceptions import NotFound

class AddCommentView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        post_id = self.request.data.get('post_id')
        if not Post.objects.filter(id=post_id).exists():
            raise NotFound("Post not found.")
        serializer.save(user=self.request.user)

class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

class PostListView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.prefetch_related(
            Prefetch(
                'comments',
                queryset=Comment.objects.order_by('-timestamp'),
                to_attr='latest_comments'
            )
        ).order_by('-timestamp')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
