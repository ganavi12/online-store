from django.shortcuts import render
from .models import Product,Manufacturer
# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
from django.views.generic import ListView, DetailView,CreateView


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"

class ProductListView(ListView): 
    model = Product
    template_name = "products/product_list.html"

