from rest_framework.decorators import api_view
from rest_framework import status, generics
from rest_framework.response import Response

import logging

from .models import Menu
from .serializers import MenuSerializer, ResultSerializer
from .queries import company_year


# Create your views here.

log = logging.getLogger('main')


class MenuListView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


@api_view(["GET"])
def company_view(request, company_id):
    log.info("%s %s", request.method, request.build_absolute_uri())
    params = request.query_params
    year = params.get('year')
    month = params.get('month')
    week = params.get('week')

    if year is None:
        return Response({'message': 'Year Parameter Required'})
    else:
        if month is None:
            # Retrieve the data of all the months of that year
            data = company_year(year, company_id)
            serializer = ResultSerializer(data)

            return Response(serializer.data, status=status.HTTP_302_FOUND)
        else:
            if week is None:
                # Retrieve the data of all the days of that month of that year
                pass
            else:
                # Retrieve the data of all the days of that week of that month
                pass


@api_view(["GET"])
def branch_view(request, branch_id):
    log.info("%s %s", request.method, request.build_absolute_uri())
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
    log.info("%s %s", request.method, request.build_absolute_uri())
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
