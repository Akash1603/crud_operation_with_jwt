from rest_framework import serializers


class CreateCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()


class CreateProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    category_id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.IntegerField()


class ListAndDetailProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    price = serializers.IntegerField()
    category = CreateCategorySerializer()


class UpdateProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField()
    price = serializers.IntegerField()
