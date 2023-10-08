from django.urls import path
from .views import ProductFormView


urlpatterns = [
    path('', ProductFormView.as_view(), name="product_form"),

]