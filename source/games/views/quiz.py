from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import date
from accounts.serializers import UserProfileSerializer
import random

from games.models import QuizQuestion, QuizHistory


class DailyQuizView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if QuizHistory.objects.filter(user=request.user, date=date.today()).exists():
            return Response({"detail": "Квиз уже пройден"}, status=400)

        questions = QuizQuestion.objects.order_by("?")[:3]
        data = [
            {
                "id": q.id,
                "question": q.question,
                "options": {
                    "A": q.option_a,
                    "B": q.option_b,
                    "C": q.option_c,
                    "D": q.option_d,
                }
            }
            for q in questions
        ]
        return Response(data)

    def post(self, request):
        if QuizHistory.objects.filter(user=request.user, date=date.today()).exists():
            return Response({"detail": "Квиз уже пройден"}, status=400)

        answers = request.data.get("answers", {})  # {question_id: "A", ...}
        correct_count = 0

        for qid, answer in answers.items():
            try:
                question = QuizQuestion.objects.get(id=qid)
                if question.correct_option.upper() == answer.upper():
                    correct_count += 1
            except QuizQuestion.DoesNotExist:
                continue

        reward = correct_count * 100
        request.user.beans += reward
        request.user.beans_total += reward
        request.user.save()

        QuizHistory.objects.create(user=request.user, correct_answers=correct_count)

        return Response({
            "correct": correct_count,
            "reward": reward,
            "profile": UserProfileSerializer(request.user).data
        })
