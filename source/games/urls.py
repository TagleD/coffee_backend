from django.urls import path

from games.views import DailySpinView, DailyQuizView

urlpatterns = [
    path("daily_spin/", DailySpinView.as_view()),
    path("daily_quiz/", DailyQuizView.as_view()),
]
