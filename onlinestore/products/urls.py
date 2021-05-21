from django.urls import path
from . import views

urlpatterns = [
   path('products/<int:pk>/', views.ProductDetailView.as_view(),name="product_detail"),
   path('', views.ProductListView.as_view(),name="product_list"), 
]
