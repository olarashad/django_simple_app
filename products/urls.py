from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_products, name="product_list"),
    path("products/new/", views.create_product, name="product_create"),
    path("products/<int:pk>/", views.show_product, name="product_detail"),
    path("products/<int:pk>/edit/", views.edit_product, name="product_edit"),
    path("products/<int:pk>/delete/", views.delete_product, name="product_delete"),
]
