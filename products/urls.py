from django.urls import path
from .views import ProductListAPIView, ProductSearchAPIView

urlpatterns = [
    path("", ProductListAPIView.as_view(), name="product-list"),
    path("search/", ProductSearchAPIView.as_view(), name="product-search"),
]