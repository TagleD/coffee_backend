from django.urls import path

from games.views import DailySpinView

urlpatterns = [
    path("daily_spin/", DailySpinView.as_view()),
]
