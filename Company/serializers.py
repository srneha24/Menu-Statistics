from rest_framework import serializers
from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    branch_name = serializers.CharField(source='branch.branch_name',read_only=True)

    class Meta:
        model = Menu
        fields = ['id', 'menu_name', 'branch','branch_name']
