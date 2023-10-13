from django.urls import path
from .views import ProductFormView, ProductListView, ProductDetailView


urlpatterns = [
    path('', ProductListView.as_view(), name="product_list"),
    path('post/', ProductFormView.as_view(), name="product_form"),
    path('<int:pk>/', ProductDetailView.as_view(), name="product_detail"),

]