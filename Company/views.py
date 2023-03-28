import logging
import datetime

from django.db.models import F
from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import Menu, HitDate
from .queries import Queries, FillMissingDates
from .serializers import MenuSerializer, HitSerializer
from .serializers import ResultSerializer, MenuResultSerializer

# Create your views here.

log = logging.getLogger('main')


class MenuListView(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


@api_view(["GET"])
@extend_schema(responses=ResultSerializer)
def company_view(request, company_id):
    log.info("%s %s", request.method, request.build_absolute_uri())

    params = request.query_params
    year = params.get('year')
    month = params.get('month')
    week = params.get('week')

    return get_data(company_id, year, month, week, 1)


@api_view(["GET"])
@extend_schema(responses=ResultSerializer)
def branch_view(request, branch_id):
    log.info("%s %s", request.method, request.build_absolute_uri())

    params = request.query_params
    year = params.get('year')
    month = params.get('month')
    week = params.get('week')

    return get_data(branch_id, year, month, week, 2)


@api_view(["GET"])
@extend_schema(responses=MenuResultSerializer)
def menu_view(request, branch_id):
    log.info("%s %s", request.method, request.build_absolute_uri())

    params = request.query_params
    year = params.get('year')
    month = params.get('month')
    week = params.get('week')

    return get_data(branch_id, year, month, week, 3)


def get_data(stats_for_id, year, month, week, stats_for):
    query = Queries(stats_for_id, stats_for)

    if year is None:
        return Response({'message': 'Year Parameter Required'})
    else:
        if month is None:
            # Retrieve the data of all the months of that year
            data = query.for_year(year)
        else:
            if week is None:
                # Retrieve the data of all the days of that month of that year
                data = query.for_month(year, month)
            else:
                # Retrieve the data of all the days of that week of that month
                data = query.for_week(year, month, week)

        """
        stats_for -->
            1 = Company
            2 = Branch
            3 = Menu
        """

        retrieved_data = None

        if stats_for == 3 and len(data) == 0:
            retrieved_data = query.empty_menu(stats_for_id)
            return Response(retrieved_data, status=status.HTTP_200_OK)

        fill_missing_dates = FillMissingDates(query.get_start_date(), query.get_end_date())

        if stats_for == 1 or stats_for == 2:
            serializer = ResultSerializer(data, many=True)
            retrieved_data = fill_missing_dates.for_company_and_branch(serializer.data)
        elif stats_for == 3:
            serializer = MenuResultSerializer(data)
            retrieved_data = fill_missing_dates.for_menu(serializer.data)

        return Response(retrieved_data, status=status.HTTP_302_FOUND)


class HitRetrieveView(generics.RetrieveAPIView):
    queryset = HitDate.objects.all()
    serializer_class = HitSerializer

    def retrieve(self, request, *args, **kwargs):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        menu = get_object_or_404(Menu, pk=kwargs.get('pk'))
        try:
            hit = HitDate.objects.get(menu=menu, date=current_date)
            if hit:
                hit.count = F('count') + 1
                hit.save()
        except:
            HitDate.objects.create(menu=menu, count=1, date=current_date)
        return Response({"message": "API Hit"})
