from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


UserModels = get_user_model()


class SpinHistory(models.Model):
    user = models.ForeignKey(
        UserModels,
        on_delete=models.CASCADE,
        related_name="spin_history",
    )
    date = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата",
    )
    reward = models.IntegerField(
        blank=False,
        null=False,
        verbose_name="Выигрыш",
    )

    class Meta:
        unique_together = ("user", "date")
        verbose_name = "История прокрутки"
        verbose_name_plural = "Истории прокрутки"