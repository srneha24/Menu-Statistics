from django.db import models

# Create your models here.


class Company(models.Model):
    company_name = models.CharField(max_length=150, unique=True, null=False, blank=False)

    def __str__(self):
        return self.company_name

    class Meta:
        managed = True
        db_table = 'company'


class Branch(models.Model):
    branch_name = models.CharField(max_length=150, unique=True, null=False, blank=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False, blank=False)
    location = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.branch_name

    class Meta:
        managed = True
        db_table = 'branch'


class Menu(models.Model):
    menu_name = models.CharField(max_length=150, unique=True, null=False, blank=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=False, blank=False)
    count = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.menu_name

    class Meta:
        managed = True
        db_table = 'menu'


class HitDate(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=False, blank=False)
    count = models.IntegerField(null=False, blank=False, default=0)
    date = models.DateField(null=False, blank=False)

    class Meta:
        managed = True
        db_table = 'hit_date'
