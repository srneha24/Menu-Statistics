from rest_framework import serializers

from .models import Menu, HitDate
from .custom_models import QueryObject


class MenuSerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source='branch.branch_name', read_only=True)

    class Meta:
        model = Menu
        fields = ['id', 'menu_name', 'branch', 'branch_name']


class ResultSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    count = serializers.IntegerField()

    class Meta:
        model = QueryObject
        fields = ["date", "count"]


class MenuResultSerializer(serializers.Serializer):
    menu_name = serializers.CharField()
    date = serializers.DateField()
    sum = serializers.IntegerField()

    def to_representation(self, queryset):
        data = {}
        for obj in queryset:
            menu_name = obj.menu_name
            date = obj.date
            count = obj.sum
            if menu_name not in data:
                data[menu_name] = []
            data[menu_name].append({"date": date, "count": count})
        return data


class HitSerializer(serializers.ModelSerializer):
    menu_name = serializers.CharField(source='menu.menu_name', read_only=True)

    class Meta:
        model = HitDate
        fields = ['id', 'menu', 'menu_name', 'count', 'date']
