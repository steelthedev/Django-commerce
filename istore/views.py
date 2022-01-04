from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, response
from .serializers import *
from django.db.models import Q
# Create your views here.


@api_view(['GET',])
def LatestProductView(request):
    try:
        product = Product.objects.all()[0:4]
    except product.DoesNotExist:
        return HttpResponse( status = 404 )
    if request.method == "GET":
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def DescriptionView(request,slug):
    try:
        product = Product.objects.get(slug = slug)
    except product.DoesNotExist:
        return HttpResponse(status= 404 )
    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)

@api_view(['GET',])
def ViewCart(request):
    user=request.user
    customer=request.user.profile
    try:
        order=Order.objects.get(customer=customer,user=user,complete=False)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)
    if request.method == "GET":
        serializer = OrderSerializer(order)
        return Response(serializer.data)

@api_view(['POST'])
def Search(request):
    if request.method == "POST":
        q = request.data.get('query', '')
        if q:
            try:
                products = Product.objects.filter(Q(name__icontains=q) | Q(description__icontains = q))
            except products.DoesNotExist:
                return HttpResponse(status=404)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        else:
            return Response({"products":[]})



        
