from rest_framework import serializers
from .models import Post, Comment, Category, Likes
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'posts']

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.StringRelatedField(many=True, read_only=True)
    likes = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ['id', 'image', 'title', 'body',  'owner', 'likes',  'comments','categories']

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ['id', 'body', 'owner', 'post']        

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Likes
        fields = ['owner', 'post']