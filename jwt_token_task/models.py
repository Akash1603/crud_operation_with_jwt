from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "category"

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        db_table = "product"

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_category", null=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name
