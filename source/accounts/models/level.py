from django.db import models


class Level(models.Model):
    number = models.PositiveIntegerField(
        unique=True,
        blank=False,
        null=False,
        verbose_name="Уровень",
    )
    beans_required = models.PositiveIntegerField(
        null=False,
        blank=False,
        verbose_name="Количество beans для достижения этого уровня"
    )

    class Meta:
        ordering = ["number"]
        verbose_name = "Уровень"
        verbose_name_plural = "Уровни"

    def __str__(self):
        return f"Level {self.number} — {self.beans_required} beans"
