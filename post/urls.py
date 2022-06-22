from django.urls import path
from .views import PostList, PostDetail, CommentList, CommentDetail, CategoryList, CategoryDetail

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/<int:pk>/',CommentDetail.as_view()),
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),
]   