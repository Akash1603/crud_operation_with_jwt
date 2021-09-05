from django.db import IntegrityError
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from service_objects.services import Service

from jwt_token_task.models import Category, Product
from jwt_token_task.serializers import CreateCategorySerializer, ListAndDetailProductSerializer


class CreateCategoryService(Service):
    """
    This class is created to create a category.
    """

    def process(self):
        try:
            category = Category.objects.create(name=self.data.get("name"))
            return Response({"category_id": category.id}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({"Error": "category already exist."}, status=status.HTTP_400_BAD_REQUEST)


class ListCategoryService(Service):
    """
    This class is created to fetch category list.
    """

    def process(self):
        return Response(CreateCategorySerializer(Category.objects.all(), many=True).data, status=status.HTTP_200_OK)


class DetailCategoryService(Service):
    """
    This class is created to fetch category detail.
    """

    def process(self):
        try:
            return Response(CreateCategorySerializer(Category.objects.get(id=self.data.get("category_id"))).data,
                            status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"Error": "Category does not exist."}, status=status.HTTP_404_NOT_FOUND)


class UpdateCategoryService(Service):
    """
    This class is created to update a category.
    """

    def process(self):
        try:
            category = Category.objects.get(id=self.data.get("category_id"))
            category.name = self.data.get("name")
            category.save()
            return Response({}, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"Error": "Category does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except IntegrityError:
            return Response({"Error": "category already exist."}, status=status.HTTP_400_BAD_REQUEST)


class DeleteCategoryService(Service):
    """
    This class is created to delete a category.
    """

    def process(self):
        try:
            Category.objects.get(id=self.data.get("category_id")).delete()
            return Response({}, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"Error": "Category does not exist."}, status=status.HTTP_404_NOT_FOUND)


class CreateProductService(Service):
    """
    This class is created to create a product.
    """

    def process(self):
        try:
            data = self.data.get("product_data")
            product = Product.objects.create(
                category=Category.objects.get(id=data.get("category_id")),
                name=data.get("name"), price=data.get("price"))
            return Response({"product_id": product.id}, status=status.HTTP_201_CREATED)
        except Category.DoesNotExist:
            return Response({"Error": "Category does not exist."}, status=status.HTTP_404_NOT_FOUND)


class ListProductService(Service):
    """
    This class is created to fetch product list.
    """

    def process(self):
        category = Category.objects.filter(name__iexact=self.data.get("category_name")).first()
        query = Q()
        if category:
            query = Q(category=category)
        return Response(
            ListAndDetailProductSerializer(Product.objects.filter(query), many=True).data,
            status=status.HTTP_200_OK)


class DetailProductService(Service):
    """
    This class is created to fetch product detail.
    """

    def process(self):
        try:
            return Response(ListAndDetailProductSerializer(Product.objects.get(id=self.data.get("product_id"))).data,
                            status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"Error": "Product does not exist."}, status=status.HTTP_404_NOT_FOUND)


class UpdateProductService(Service):
    """
    This class is created to update a product.
    """

    def process(self):
        try:
            data = self.data.get("product_data")
            product = Product.objects.get(id=self.data.get("product_id"))
            product.name = data.get("name")
            product.price = data.get("price")
            product.save()
            return Response({}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"Error": "Category does not exist."}, status=status.HTTP_404_NOT_FOUND)


class DeleteProductService(Service):
    """
    This class is created to delete a product.
    """

    def process(self):
        try:
            Product.objects.get(id=self.data.get("product_id")).delete()
            return Response({}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"Error": "Product does not exist."}, status=status.HTTP_404_NOT_FOUND)
