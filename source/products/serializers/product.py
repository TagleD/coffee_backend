from rest_framework import serializers

from .tag import TagSerializer
from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'bean_price',
            'image',
            'tags',
            'is_active',
        ]
