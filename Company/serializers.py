from rest_framework import serializers
from .models import Menu,HitDate


class MenuSerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source='branch.branch_name', read_only=True)

    class Meta:
        model = Menu
        fields = ['id', 'menu_name', 'branch', 'branch_name']


class HitSerializer(serializers.ModelSerializer):
    menu_name = serializers.CharField(source='menu.menu_name', read_only=True)

    class Meta:
        model = HitDate
        fields = ['id', 'menu', 'menu_name', 'count', 'date']
