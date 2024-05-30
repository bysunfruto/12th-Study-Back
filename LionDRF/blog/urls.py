from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),  # 전체 게시물 조회 및 키워드 검색
    path('create/', PostList.as_view(), name='post-create'),  # 새로운 게시물 생성
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),  # 특정 게시물 조회, 수정, 삭제
]