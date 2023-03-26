from django.contrib import admin

from .models import Company, Branch, Menu, HitDate

# Register your models here.

admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(Menu)
admin.site.register(HitDate)
