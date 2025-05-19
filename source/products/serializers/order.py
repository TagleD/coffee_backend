from decimal import Decimal

from rest_framework import serializers

from products.models import Order, OrderItem
from products.serializers.order_item import OrderItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "items", "created_at", "total_price", "beans_earned"]

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user

        items_data = validated_data.pop("items")

        total_price = sum(item["price_per_item"] * item["quantity"] for item in items_data)

        order = Order.objects.create(user=user, total_price=total_price)

        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)

        # начисление beans
        beans = int(total_price * Decimal("0.1"))
        user.beans += beans
        user.beans_total += beans
        user.save()

        order.beans_earned = beans
        order.save()

        return order