from django.db import models


class QueryObject(models.Model):
    date = models.DateField(null=False, blank=False)
    count = models.IntegerField(null=False, blank=False, default=0)
    branch_name = models.CharField(max_length=150, unique=True, null=False, blank=False)
    menu_name = models.CharField(max_length=150, unique=True, null=False, blank=False)
