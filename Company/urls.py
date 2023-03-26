from django.urls import path
from .views import (
    company_view,
    branch_view,
    menu_view,
    MenuListView,
    MenuCreateView
)

app_name = "Company"

urlpatterns = [
    path('<int:company_id>/', company_view, name="CompanyStatistics"),
    path('branch/<int:branch_id>/', branch_view, name="BranchStatistics"),
    path('branch/menu/<int:branch_id>/', menu_view, name="MenuStatistics"),
    path('menus/', MenuListView.as_view(), name="menu_list"),
    path('menu-create/', MenuCreateView.as_view(), name="menu_create"),
]