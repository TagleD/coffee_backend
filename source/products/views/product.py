from django.db.models import Q
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product
from products.serializers.product import ProductSerializer


class ProductListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        search = request.GET.get('search', '').strip()
        tag_code = request.GET.get('tag', '').strip()

        products = Product.objects.filter(is_active=True)

        if search:
            products = products.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search) |
                Q(tags__name__icontains=search)
            )

        if tag_code:
            products = products.filter(tags__code=tag_code)

        products = products.distinct().order_by('created_at')

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
