from django.db import models


class Tag(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Наименование",
    )
    code = models.SlugField(
        max_length=100,
        null=False,
        blank=False,
        unique=True,
        verbose_name="Уникальный код на латинице",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at",
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
