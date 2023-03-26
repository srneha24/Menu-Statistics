from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status, generics
from rest_framework.response import Response

import logging
from django.db.models import F

# Create your views here.
from Company.models import Menu, HitDate
from Company.serializers import MenuSerializer, HitSerializer

log = logging.getLogger('main')


class MenuListView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


@api_view(["GET"])
def company_view(request, company_id):
    params = request.query_params
    year = params.get('year')
    month = params.get('month')
    week = params.get('week')

    if year is None:
        return Response({'message': 'Year Parameter Required'})
    else:
        if month is None:
            # Retrieve the data of all months of that year
            pass
        else:
            if week is None:
                # Retrieve the data of all the days of that month of that year
                pass
            else:
                # Retrieve the data of all the days of that week of that month
                pass


@api_view(["GET"])
def branch_view(request, branch_id):
    params = request.query_params
    year = params.get('year')
    month = params.get('month')
    week = params.get('week')

    if year is None:
        return Response({'message': 'Year Parameter Required'})
    else:
        if month is None:
            # Retrieve the data of all months of that year
            pass
        else:
            if week is None:
                # Retrieve the data of all the days of that month of that year
                pass
            else:
                # Retrieve the data of all the days of that week of that month
                pass


@api_view(["GET"])
def menu_view(request, branch_id):
    params = request.query_params
    year = params.get('year')
    month = params.get('month')
    week = params.get('week')

    if year is None:
        return Response({'message': 'Year Parameter Required'})
    else:
        if month is None:
            # Retrieve the data of all months of that year
            pass
        else:
            if week is None:
                # Retrieve the data of all the days of that month of that year
                pass
            else:
                # Retrieve the data of all the days of that week of that month
                pass


class MenuCreateView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class HitRetrieveView(generics.RetrieveAPIView):
    queryset = HitDate.objects.all()
    serializer_class = HitSerializer

    def retrieve(self, request, *args, **kwargs):
        menu = get_object_or_404(HitDate, pk=kwargs.get('pk'))
        menu.count = F('count') + 1
        menu.save()
        return Response({'hit!!!'})
