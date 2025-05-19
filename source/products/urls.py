from django.urls import path

from products.views import (
    ProductListView, TagListView,
    CreateOrderView, OrderHistoryView,
)

urlpatterns = [
    path("products/", ProductListView.as_view()),
    path("tags/", TagListView.as_view()),
    path("create_order/", CreateOrderView.as_view()),
    path("order_history/", OrderHistoryView.as_view()),
]
