from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="Название товара",
    )
    description = models.TextField(
        null=False,
        blank=False,
        verbose_name="Описание товара",
    )
    price = models.IntegerField(
        null=False,
        verbose_name="Стоимость тг.",
    )
    bean_price = models.IntegerField(
        null=False,
        verbose_name="Стоимость bean coins",
    )
    image = models.ImageField(
        upload_to="product_images/",
        blank=False,
        null=False,
        verbose_name="Картинка товара",
    )
    tags = models.ManyToManyField(
        "Tag",
        related_name="products",
        blank=False,
    )
    is_active = models.BooleanField(
        blank=False,
        null=False,
        default=True,
        verbose_name="Активен",
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
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
