from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Product, Message
from .serializer import ProductSerializer

@api_view(['GET'])

def getData(request):
    data = {"message": "Hello from Django!"}
    return Response(data)

class ProductListAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        search_query = self.request.query_params.get('search')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        return queryset
    


@api_view(['POST'])
def send_message(request):
    name = request.data.get('name')
    email = request.data.get('email')
    content = request.data.get('content')

    Message.objects.create(name=name, email=email, content=content)

    return Response({'success': True, 'message' : 'Xabar muvaffaqiyatli yuborildi!'})