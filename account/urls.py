from django.urls import path
from .views import UserCreateAPIView, UserLoginAPIView, UserDetailAPIView

urlpatterns = [
   path('register/', UserCreateAPIView.as_view()),
   path('login/', UserLoginAPIView.as_view()),
   path('users/', UserDetailAPIView.as_view()),
]