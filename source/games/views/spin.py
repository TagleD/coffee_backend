# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import date
import random

from accounts.serializers import UserProfileSerializer
from games.models import SpinHistory


class DailySpinView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        # Проверка: уже крутил?
        if SpinHistory.objects.filter(user=user, date=date.today()).exists():
            return Response({"detail": "Вы уже крутили сегодня"}, status=400)

        # Вычисление награды (шансы уменьшаются с ростом значения)
        reward = random.choices(
            population=[50, 100, 200, 300, 500, 1000],
            weights=[1, 1, 2, 2, 1, 1],
            k=1
        )[0]

        # Обновим beans и beans_total
        user.beans += reward
        user.beans_total += reward
        user.save()

        # Сохраним историю
        SpinHistory.objects.create(user=user, reward=reward)

        return Response({
            "beans_won": reward,
            "new_beans": user.beans,
            "profile": UserProfileSerializer(user).data
        })