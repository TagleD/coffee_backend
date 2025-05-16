from django.urls import path

from products.views import ProductListView, TagListView, CreateOrderView

urlpatterns = [
    path("products/", ProductListView.as_view()),
    path("tags/", TagListView.as_view()),
    path("create_order/", CreateOrderView.as_view()),
]
