from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from .models import Product
from .serializers import ProductSerializer
from .services import calculate_relevance
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# -------------------------
# List All Products
# -------------------------

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


# -------------------------
# Search Products
# -------------------------

class ProductSearchAPIView(APIView):

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
    operation_description="Search products by keyword",
    manual_parameters=[
        openapi.Parameter(
            "q",
            openapi.IN_QUERY,
            description="Search keyword",
            type=openapi.TYPE_STRING,
            required=True,
        ),
        openapi.Parameter(
            "limit",
            openapi.IN_QUERY,
            description="Maximum number of results",
            type=openapi.TYPE_INTEGER,
            required=False,
        ),
        openapi.Parameter(
            "category_filter",
            openapi.IN_QUERY,
            description="Filter by category",
            type=openapi.TYPE_STRING,
            required=False,
        ),
    ],
)

    def get(self, request):

        query = request.GET.get("q")

        if not query:
            return Response(
                {"error": "Query parameter 'q' is required."},
                status=400
            )

        limit = int(request.GET.get("limit", 20))

        category_filter = request.GET.get("category_filter")

        products = Product.objects.filter(
            Q(category__icontains=query) |
            Q(tags__icontains=query) |
            Q(product_name__icontains=query) |
            Q(product_description__icontains=query)
        )

        if category_filter:
            products = products.filter(category__iexact=category_filter)

        ranked_results = []

        for product in products:
            score, reason = calculate_relevance(product, query)

            if score > 0:
                ranked_results.append({
                    "id": product.id,
                    "product_name": product.product_name,
                    "category": product.category,
                    "tags": product.tags.split(","),
                    "relevance_score": score,
                    "rank_reason": reason,
                })

        ranked_results.sort(
            key=lambda x: x["relevance_score"],
            reverse=True
        )

        return Response({
            "query": query,
            "total_results": len(ranked_results),
            "results": ranked_results[:limit]
        })