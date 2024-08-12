from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('product/',views.get_all_products,name='product'),
    path('product/<str:pk>',views.get_by_id_product,name='product'),
]
