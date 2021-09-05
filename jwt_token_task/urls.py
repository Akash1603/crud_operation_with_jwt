from django.urls import path

from jwt_token_task.views import CategoryCreateAndListViews, CategoryDetailUpdateDeleteViews, ProductCreateAndListViews, \
    ProductDetailUpdateDeleteViews

urlpatterns = [
    # Category model URLS.
    path('category/', CategoryCreateAndListViews.as_view(), name="category_create_and_list"),
    path('category/<int:category_id>/', CategoryDetailUpdateDeleteViews.as_view(),
         name="category_detail_update_and_delete"),
    # Product model URLS.
    path('product/', ProductCreateAndListViews.as_view(), name="product_create_and_list"),
    path('product/<int:product_id>/', ProductDetailUpdateDeleteViews.as_view(),
         name="product_detail_update_and_delete"),
]
