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
        views.CategoryAPIView.as_view(),
        name='category-list'
    ),
    path(
        "<int:id>/",
        views.ProductUpdateDeleteAPIView.as_view(),
        name="product-update-del"
    ),
    path(
        "categories/<int:id>",
        views.CategoryUpdateDeleteAPIView.as_view(),
        name="category-update-del"
    ),
    path(
        "search/", views.SearchAPIView.as_view()
    )
]

