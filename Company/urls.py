from django.urls import path

from .views import (
    company_view,
    branch_view,
    menu_view,
    hit_api,
    MenuListView
)

app_name = "Company"

urlpatterns = [
    path('<int:company_id>/', company_view, name="CompanyStatistics"),
    path('branch/<int:branch_id>/', branch_view, name="BranchStatistics"),
    path('branch/menu/', hit_api, name="HitAPI"),
    path('branch/menu/<int:branch_id>/', menu_view, name="MenuStatistics"),
    path('menu/', MenuListView.as_view(), name="MenuList")
]