from rest_framework import serializers
from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    branch = serializers.CharField(source='branch.branch_name')

    class Meta:
        model = Menu
        fields = ['id', 'menu_name', 'branch']
