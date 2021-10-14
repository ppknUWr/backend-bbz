from django.urls import path
from authentication.views import UserRegistrationAPIView, UserLoginAPIView, UserTokenAPIView


urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
    path('tokens/', UserTokenAPIView.as_view()),
]

