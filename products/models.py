from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=255)

    product_description = models.TextField()

    category = models.CharField(max_length=100, db_index=True)

    tags = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=["category"]),
        ]

    def __str__(self):
        return self.product_name