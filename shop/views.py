from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from .models import Product
from .forms import FileFieldForm

class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
class ProductFormView(FormView):
    form_class = FileFieldForm
    template_name = "product_form.html"
    success_url = "success"

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        files = form.cleaned_data["file_field"]
        product = Product.objects.create(
            title = form.cleaned_data['title'],
            description= form.cleaned_data['description'],
            thumbnail= files[0],
        )
        files.pop(0)
        for f in files:
            product.image_set.create(image=f)
        return super().form_valid(form)