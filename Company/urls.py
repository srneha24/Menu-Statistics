from django.urls import path
from .views import (
    company_view,
    branch_view,
    menu_view,
    MenuListView,
    HitRetrieveView,
)

app_name = "Company"

urlpatterns = [
    path('<int:company_id>/', company_view, name="CompanyStatistics"),
    path('branch/<int:branch_id>/', branch_view, name="BranchStatistics"),
    path('branch/menu/<int:branch_id>/', menu_view, name="MenuStatistics"),
    path('branch/menu/', MenuListView.as_view(), name="menu_list"),
    path('branch/menu/hits/<str:pk>/', HitRetrieveView.as_view(), name="hit_retrieve"),
]
