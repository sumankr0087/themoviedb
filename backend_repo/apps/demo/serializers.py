from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    post_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'timestamp', 'username', 'post_id']
        read_only_fields = ['id', 'timestamp', 'username']

    def create(self, validated_data):
        user = self.context['request'].user
        post_id = validated_data.pop('post_id')
        post = Post.objects.get(id=post_id)
        comment = Comment.objects.create(user=user, post=post, **validated_data)
        return comment


class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    comments = serializers.SerializerMethodField()
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'text', 'timestamp', 'username', 'comment_count', 'comments']
        read_only_fields = ['timestamp', 'username', 'comment_count', 'comments']

    def get_comments(self, obj):
        comments = obj.comments.order_by('-timestamp')[:3]
        return CommentSerializer(comments, many=True).data

    def create(self, validated_data):
        user = self.context['request'].user
        post = Post.objects.create(user=user, **validated_data)
        return post
