from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Tag
from products.serializers.tag import TagSerializer


class TagListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)