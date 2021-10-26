from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model


# author 필드를 가져오기 위한 User모델
User = get_user_model()

# User모델 데이터(author 정보) 추출을 위한 Serializer
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class CommentListSerializer(serializers.ModelSerializer):
    # User모델의 데이터
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'author',
            'content'
        ]


class PostListSerializer(serializers.ModelSerializer):
    # 불러온 데이터들이 fields에 없는 경우 추가 필수

    #1) User 모델의 데이터
    author = UserSerializer(read_only=True)

    #2) comment 데이터
    # comment_set = CommentListSerializer(read_only=True, many=True)

    #3) comment 개수
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'author',
            'comment_count'
        ]


class PostSerializer(serializers.ModelSerializer):
    # fields를 '__all__'로 설정한 경우 fields에 추가 불필요

    #1) User 데이터
    author = UserSerializer(read_only=True)

    #2) Comment 데이터
    comment_set = CommentListSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = '__all__'
