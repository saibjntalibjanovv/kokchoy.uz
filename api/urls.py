from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('messages/', views.send_message, name = 'send_message')
]