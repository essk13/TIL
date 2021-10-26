from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from .models import Post, Comment
from .serializers import ( PostListSerializer,
                           PostSerializer,
                          )


User = get_user_model()

# api_view 데코레이터 필수
@api_view(['GET', 'POST'])
def post_list_create(request):
    user = get_object_or_404(User, pk=1)
    # 조회
    if request.method == 'GET':
        posts = get_list_or_404(Post)
        # 복수자료 serializer 시 many=True 옵션 필수
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

    # 생성
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        # raise_exception 옵션은 에러 발생시 조치사항
        if serializer.is_valid(raise_exception=True):
            # author 정보 수동 저장
            serializer.save(author=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # raise_exception 미작성 시 작성 필요
        # return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail_update_delete(request, post_pk):
    # 조회할 post 데이터
    post = get_object_or_404(Post, pk=post_pk)

    # 상세 조회
    if request.method == 'GET':
        # 단수자료 serializer 시 many=True 옵션 불필요
        serializer = PostSerializer(post)
        return Response(serializer.data)

    # 수정
    elif request.method == 'PUT':
        # 첫번째 인자 = instance=수정할 원본 데이터
        # 두번째 인자 = data=request.data
        # api_view 데코레이터가 data자료로 변환하기 때문에 request.POST가 아닌 request.data 사용
        serializer = PostSerializer(instance=post, data=request.data)

        # raise_exception 옵션은 에러 발생시 조치사항
        if serializer.is_valid(raise_exception=True):
            # author 정보가 이미 존재함으로 추가 저장 불필요
            serializer.save()
            return Response(serializer.data)

        # raise_exception 미작성 시 작성 필요
        # return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    # 삭제
    elif request.method == 'DELETE':
        author = post.author
        title = post.title
        post.delete()
        data = {
            'msg': f'{author}님의 {title} 포스트가 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
