from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title',
                  'description',
                  'price',
                  'discount',
                  'image',
                  'created',
                  'updated',
                  'category']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductValidateSerializer(serializers.Serializer):
    image = serializers.ImageField(required=False)
    title = serializers.CharField(required=True, max_length=250)
    price = serializers.IntegerField(required=False, default=0)
    amount = serializers.IntegerField(required=False, default=0)
    category = serializers.ListField(required=False, child=serializers.CharField())
    discount = serializers.BooleanField(required=False, default=False)

    def validate_title(self, title):
        title_exists = Product.objects.filter(title=title).exists()
        if not title_exists:
            return title
        raise ValidationError("Product with this title already exists")

    def create(self, validated_data):
        return Product.objects.create(**validated_data)


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)

    def validate_name(self, name):
        title_exists = Category.objects.filter(name=name).exists()
        if not title_exists:
            return name
        raise ValidationError("Category with this name already exists")

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class SearchSerializer(serializers.Serializer):
    def validate_search(self, obj):
        if isinstance(obj, Product):
            serializer = ProductSerializer(obj)
        elif isinstance(obj, Category):
            serializer = CategorySerializer(obj)
        else:
            raise Exception("Nothing found!")
        return serializer.data

