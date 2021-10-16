from django.urls import path
from . import views

urlpatterns = [
    path('product_list/', views.products, name='products'),  # Redirect to products page
    path('product_details/<int:product_id>', views.product_details, name='product_details'),  # Visit Specific product by ID
]