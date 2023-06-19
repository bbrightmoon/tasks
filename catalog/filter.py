from django_filters import rest_framework as filter

from catalog.models import Product


class CategoryFilter(filter.BaseInFilter, filter.CharFilter):
    pass


class ProductFilter(filter.FilterSet):
    price = filter.RangeFilter()
    category = CategoryFilter(field_name='category__name')
    discount = filter.BooleanFilter()

    class Meta:
        model = Product
        fields = ['price', ]