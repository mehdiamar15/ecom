from django.shortcuts import get_object_or_404,render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .filtters import ProductsFilter
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Avg
# Create your views here.


@api_view(['GET'])
def get_all_products(request):
   #filer option https://django-filter.readthedocs.io/en/stable/
   filterset = ProductsFilter(request.GET,queryset=Product.objects.all().order_by('id'))
   count = filterset.qs.count()
   resPage = 2
   paginator = PageNumberPagination()
   paginator.page_size = resPage
   
   queryset =  paginator.paginate_queryset(filterset.qs, request)
   serializer = ProductSerializer(queryset,many=True)
   return Response({"products":serializer.data, "per page":resPage, "count":count})
# Create your views here.

@api_view(['GET'])
def get_by_id_product(request,pk):
    products = get_object_or_404(Product,id=pk)
    serializer = ProductSerializer(products,many=False)
    print(products)
    return Response({"product":serializer.data})