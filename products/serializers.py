from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    tags = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "product_name",
            "product_description",
            "category",
            "tags",
        ]

    def get_tags(self, obj):
        return obj.tags.split(",")