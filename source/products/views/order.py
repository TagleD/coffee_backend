from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Order
from products.serializers import OrderSerializer


class CreateOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = OrderSerializer(data=request.data, context={"request": request})
        if not serializer.is_valid():
            print(serializer.errors)  # 🧠 Добавь это
            return Response(serializer.errors, status=400)
        order = serializer.save()
        return Response({
            "message": "Заказ успешно оформлен",
            "order_id": order.id,
            "beans_earned": order.beans_earned,
        })


class OrderHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
        return Response(OrderSerializer(orders, many=True).data)
