from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView

from .forms import ProductForm
from .models import Product


class HomeView(TemplateView):
    template_name = 'index.html'


class ProductInputView(FormView):
    form_class = ProductForm
    template_name = 'add_product.html'
    context_object_name = 'products'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Has añadido un producto exitosamente.')
        return redirect('list_product')


class ProductListView(ListView):
    model = Product
    template_name = 'list_product.html'
    context_object_name = 'products'


class ShowStringView(View):
    def get(self, request, query_string):
        if query_string.strip():
            context = {'query_string': query_string}
            return render(request, 'show_string.html', context)
        else:
            messages.error(request, 'La cadena no puede estar vacía o solo contener espacios.')
            return redirect('index')


class ShowDetailsProductView(View):
    def get(self, request, query_id):
        try:
            product = Product.objects.get(id=query_id)
            context = {'product': product}
            return render(request, 'show_product_by_id.html', context)
        except ObjectDoesNotExist:
            messages.error(request, 'Error: El producto no existe.')
            return redirect('index')
