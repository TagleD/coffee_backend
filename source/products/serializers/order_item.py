from rest_framework import serializers
from products.models import Product, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source="product",
        write_only=True
    )

    class Meta:
        model = OrderItem
        fields = ["product_id", "quantity", "price_per_item"]
