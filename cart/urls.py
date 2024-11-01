from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartItem.as_view(), name='cart'),
]
