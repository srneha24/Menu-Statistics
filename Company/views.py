from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

import logging


# Create your views here.

log = logging.getLogger('main')


@api_view(["POST"])
def hit_api(request):
    pass

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
