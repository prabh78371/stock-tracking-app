from functools import partial
from itertools import product
from urllib import response
from django.shortcuts import render
from itsdangerous import Serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import productserializer, stockserializer
from .models import product_model
from .serializer import productserializer
from .models import stock_tracking_model
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def product_api(request,pk=None):
    if request.method ==  'GET':
        id = pk
        if id is not None:
            prod = stock_tracking_model.objects.get(id=id)
            serilizer = stockserializer(prod)
            return Response(serilizer.data)
        prod = stock_tracking_model.objects.all()
        serilizer = stockserializer(prod,many=True)
        return Response(serilizer.data)

    if request.method == 'POST':
        serilizer = stockserializer(data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status = status.HTTP_201_CREATED)
        return Response(serilizer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def stock_api(request,pk=None):
    if request.method ==  'GET':
        id = pk
        if id is not None:
            prod = product_model.objects.get(id=id)
            serilizer = productserializer(prod)
            return Response(serilizer.data)
        prod = product_model.objects.all()
        serilizer = productserializer(prod,many=True)
        return Response(serilizer.data)

    if request.method == 'POST':
        serilizer = productserializer(data = request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status = status.HTTP_201_CREATED)
        return Response(serilizer.errors,status = status.HTTP_400_BAD_REQUEST)