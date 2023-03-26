from django.shortcuts import render
from .models import Menu
from .serializers import MenuSerializer
from rest_framework import generics


class MenuListView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
