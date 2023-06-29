from django.urls import path
from catalog import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path(
        "",
        cache_page(15)(views.ProductAPIView.as_view()),
        name="product-list"
    ),
    path(
        "categories/",
        cache_page(15)(views.CategoryAPIView.as_view()),
        name='category-list'
    ),
    path(
        "<int:id>/",
        cache_page(15)
        (views.ProductUpdateDeleteAPIView.as_view()),
        name="product-update-del"
    ),
    path(
        "categories/<int:id>/",
        cache_page(15)
        (views.CategoryUpdateDeleteAPIView.as_view()),
        name="category-update-del"
    ),
    path(
        "search/", cache_page(15)(views.SearchAPIView.as_view())
    )
]

