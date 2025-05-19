from rest_framework import serializers
from products.models import Product, OrderItem
from products.serializers.product import ProductSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # для ответа
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source="product",
        write_only=True  # для записи
    )

    class Meta:
        model = OrderItem
        fields = ["product", "product_id", "quantity", "price_per_item"]
