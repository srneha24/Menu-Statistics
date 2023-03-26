import calendar
from datetime import datetime
import logging

from .custom_models import QueryObject


def company_year(year, company_id):
    start = str(year) + "-01-01"
    end = str(year) + "-12-31"

    result = QueryObject.objects.raw("SELECT hit_date.id, hit_date.date, hit_date.count, branch.branch_name, "
                                     "menu.menu_name " +
                                     "FROM hit_date, menu, branch, company " +
                                     "WHERE company.id = %s " +
                                     "AND company.id = branch.company_id " +
                                     "AND branch.id = menu.branch_id and hit_date.menu_id = menu.id " +
                                     "AND hit_date.date BETWEEN %s AND %s " +
                                     "GROUP BY hit_date.date, menu.id, branch.id, hit_date.count, hit_date.id " +
                                     "ORDER BY hit_date.date",
                                     [company_id, start, end])

    return result


def company_month(year, month, company_id):
    start = str(year) + "-" + str(month) + "-01"
    num_days = calendar.monthrange(year, month)[1]
    end = str(year) + "-" + str(month) + "-" + str(num_days)

    result = QueryObject.objects.raw("SELECT hit_date.id, hit_date.date, hit_date.count, branch.branch_name, "
                                     "menu.menu_name " +
                                     "FROM hit_date, menu, branch, company " +
                                     "WHERE company.id = %s " +
                                     "AND company.id = branch.company_id " +
                                     "AND branch.id = menu.branch_id and hit_date.menu_id = menu.id " +
                                     "AND hit_date.date BETWEEN %s AND %s " +
                                     "GROUP BY hit_date.date, menu.id, branch.id, hit_date.count, hit_date.id " +
                                     "ORDER BY hit_date.date",
                                     [company_id, start, end])

    return result


def company_week(year, month, week, company_id):
    days_of_the_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    # month_first = str(year) + "-" + str(month) + "-01"
    # month_first_obj = datetime.strptime(month_first, '%Y-%m-%d')
    # day_of_week = month_first_obj.weekday()

    result = QueryObject.objects.raw("SELECT hit_date.id, hit_date.date, hit_date.count, branch.branch_name, "
                                     "menu.menu_name " +
                                     "FROM hit_date, menu, branch, company " +
                                     "WHERE company.id = %s " +
                                     "AND company.id = branch.company_id " +
                                     "AND branch.id = menu.branch_id and hit_date.menu_id = menu.id " +
                                     "AND hit_date.date BETWEEN %s AND %s " +
                                     "GROUP BY hit_date.date, menu.id, branch.id, hit_date.count, hit_date.id " +
                                     "ORDER BY hit_date.date",
                                     [company_id, start, end])

    return result
