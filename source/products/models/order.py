from django.contrib.auth import get_user_model
from django.db import models


class Order(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="orders",
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    beans_earned = models.IntegerField(
        default=0,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at"
    )

    def __str__(self):
        return f"Order #{self.id} by {self.user.phone}"
