from django_filters.rest_framework import DjangoFilterBackend
from catalog.serializer import (
    ProductSerializer,
    ProductValidateSerializer,
    CategorySerializer,
    CategoryValidateSerializer,
    SearchSerializer
)
from catalog.models import Product, Category
from user.permissions import Administrator, Tenant
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from catalog.filter import ProductFilter
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from drf_multiple_model.views import ObjectMultipleModelAPIView
from catalog.utils import LimitPagination
from user.models import User
from user.serializer import LoginSerializer



class ProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [Administrator, Tenant]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ProductFilter
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        else:
            return ProductValidateSerializer


class ProductUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [Tenant, Administrator]
    lookup_field = "id"
    pagination_class = PageNumberPagination
    filterset_class = ProductFilter


class CategoryAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    permission_classes = [Administrator]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['id', 'name']
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategorySerializer
        else:
            return CategoryValidateSerializer


class CategoryUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [Administrator]
    lookup_field = "id"
    pagination_class = PageNumberPagination


class SearchAPIView(ObjectMultipleModelAPIView):
    pagination_class = LimitPagination
    querylist = []
    serializer_class = SearchSerializer

    def get_querylist(self, *args, **kwargs):
        search = self.request.GET.get('search')
        print(search)
        if search:
            querylist = [
                {
                    'queryset': Product.objects.filter(Q(title__icontains=search) | Q(description__icontains=search) |
                                                       Q(category__name__icontains=search)),
                    'serializer_class': ProductSerializer,
                },
                {
                    'queryset': Category.objects.filter(Q(name__icontains=search)),
                    'serializer_class': CategorySerializer,
                },
                {
                    'queryset': User.objects.filter(Q(username__icontains=search)),
                    'serializer_class': LoginSerializer,
                }]
            return querylist

