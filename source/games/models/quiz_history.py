from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class QuizHistory(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    correct_answers = models.PositiveIntegerField()

    class Meta:
        unique_together = ("user", "date")
