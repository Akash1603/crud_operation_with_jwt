from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from jwt_token_task.controller import CreateCategoryService, ListCategoryService, DetailCategoryService, \
    UpdateCategoryService, DeleteCategoryService, CreateProductService, ListProductService, DetailProductService, \
    UpdateProductService, DeleteProductService
from jwt_token_task.serializers import CreateCategorySerializer, CreateProductSerializer, UpdateProductSerializer


class BaseView(APIView):
    permission_classes = (IsAuthenticated,)


class CategoryCreateAndListViews(BaseView):
    """
    This class is created to make create and list methods of category model.
    """

    @staticmethod
    def post(request):
        serial_data = CreateCategorySerializer(data=request.data)
        if serial_data.is_valid(raise_exception=True):
            return CreateCategoryService.execute({"name": serial_data.validated_data.get("name")})

    @staticmethod
    def get(_):
        return ListCategoryService.execute({})


class CategoryDetailUpdateDeleteViews(BaseView):
    """
    This class is created to make detail, update and delete methods of category model.
    """

    @staticmethod
    def get(_, category_id):
        return DetailCategoryService.execute({"category_id": category_id})

    @staticmethod
    def put(request, category_id):
        serial_data = CreateCategorySerializer(data=request.data)
        if serial_data.is_valid(raise_exception=True):
            return UpdateCategoryService.execute(
                {"name": serial_data.validated_data.get("name"), "category_id": category_id})

    @staticmethod
    def delete(_, category_id):
        return DeleteCategoryService.execute({"category_id": category_id})


class ProductCreateAndListViews(BaseView):
    """
    This class is created to make create and list methods of product model.
    """

    @staticmethod
    def post(request):
        serial_data = CreateProductSerializer(data=request.data)
        if serial_data.is_valid(raise_exception=True):
            return CreateProductService.execute({"product_data": serial_data.validated_data})

    @staticmethod
    def get(request):
        return ListProductService.execute({"category_name": request.GET.get("category_name")})


class ProductDetailUpdateDeleteViews(BaseView):
    """
    This class is created to make detail, update and delete methods of product model.
    """

    @staticmethod
    def get(_, product_id):
        return DetailProductService.execute({"product_id": product_id})

    @staticmethod
    def put(request, product_id):
        serial_data = UpdateProductSerializer(data=request.data)
        if serial_data.is_valid(raise_exception=True):
            return UpdateProductService.execute(
                {"product_data": serial_data.validated_data, "product_id": product_id})

    @staticmethod
    def delete(_, product_id):
        return DeleteProductService.execute({"product_id": product_id})
