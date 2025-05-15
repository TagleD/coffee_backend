from django.urls import path
from accounts.views import (
    RegisterView, LoginView,
    UserProfileView, UserUpdateView,
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('profile/update/', UserUpdateView.as_view()),
]
