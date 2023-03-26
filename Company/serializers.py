from rest_framework import serializers

from .models import Menu, HitDate


class MenuSerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source='branch.branch_name', read_only=True)

    class Meta:
        model = Menu
        fields = ['id', 'menu_name', 'branch', 'branch_name']


class CompanyResultSerializer(serializers.Serializer):
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


class BranchResultSerializer(serializers.Serializer):
    menu_name = serializers.CharField()
    date = serializers.DateField()
    count = serializers.IntegerField()

    def to_representation(self, queryset):
        data = {}
        for obj in queryset:
            menu_name = obj.menu_name
            date = obj.date
            count = obj.count
            if menu_name not in data:
                data[menu_name] = {}
            data[menu_name][str(date)] = count
        return data


class MenuResultSerializer(serializers.Serializer):
    pass


class HitSerializer(serializers.ModelSerializer):
    menu_name = serializers.CharField(source='menu.menu_name', read_only=True)

    class Meta:
        model = HitDate
        fields = ['id', 'menu', 'menu_name', 'count', 'date']
