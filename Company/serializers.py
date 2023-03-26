from django.db.models.query import RawQuerySet
from rest_framework import serializers

from .models import Menu

import logging


log = logging.getLogger('main')

class MenuSerializer(serializers.ModelSerializer):
    branch = serializers.CharField(source='branch.branch_name')

    class Meta:
        model = Menu
        fields = ['id', 'menu_name', 'branch']


class ResultSerializer(serializers.Serializer):
    branch_name = serializers.CharField()
    menu_name = serializers.CharField()
    date = serializers.DateField()
    count = serializers.IntegerField()

    def to_representation(self, queryset):
        data = {}
        for obj in queryset:
            branch_name = obj.branch_name
            menu_name = obj.menu_name
            date = obj.date
            count = obj.count
            if branch_name not in data:
                data[branch_name] = {}
            if menu_name not in data[branch_name]:
                data[branch_name][menu_name] = {}
            data[branch_name][menu_name][str(date)] = count
        return data
