import calendar
import datetime

from .models import Menu
from .custom_models import QueryObject


class Queries:
    __start = None
    __end = None

    def __company_query(self):
        result = QueryObject.objects.raw("SELECT SUM(hit_date.count), hit_date.date, company.id " +
                                         "FROM hit_date, menu, branch, company " +
                                         "WHERE company.id = %s " +
                                         "AND company.id = branch.company_id " +
                                         "AND branch.id = menu.branch_id and hit_date.menu_id = menu.id " +
                                         "AND hit_date.date BETWEEN %s AND %s " +
                                         "GROUP BY hit_date.date, company.id " +
                                         "ORDER BY hit_date.date",
                                         [self.__stats_for_id, self.__start, self.__end])

        return self.__create_model_object(result)

    def __branch_query(self):
        result = QueryObject.objects.raw("SELECT SUM(hit_date.count), hit_date.date, branch.id " +
                                         "FROM hit_date, menu, branch " +
                                         "WHERE branch.id = %s " +
                                         "AND branch.id = menu.branch_id and hit_date.menu_id = menu.id " +
                                         "AND hit_date.date BETWEEN %s AND %s " +
                                         "GROUP BY hit_date.date, branch.id " +
                                         "ORDER BY hit_date.date",
                                         [self.__stats_for_id, self.__start, self.__end])

        return self.__create_model_object(result)

    def __menu_query(self):
        result = QueryObject.objects.raw("SELECT hit_date.id, hit_date.date, SUM(hit_date.count), menu.menu_name " +
                                         "FROM hit_date, menu, branch " +
                                         "WHERE branch.id = %s " +
                                         "AND branch.id = menu.branch_id and hit_date.menu_id = menu.id " +
                                         "AND hit_date.date BETWEEN %s AND %s " +
                                         "GROUP BY hit_date.date, menu.id, branch.id, hit_date.id " +
                                         "ORDER BY hit_date.date",
                                         [self.__stats_for_id, self.__start, self.__end])

        return result

    def empty_menu(self, branch_id):
        result = Menu.objects.filter(branch_id=branch_id).order_by('menu_name').values('menu_name')

        start_date = datetime.datetime.strptime(self.__start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(self.__end, '%Y-%m-%d')

        all_dates = [start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1)]
        new_data = dict()

        for res in result:
            dates = list()
            for date in all_dates:
                dates.append({"date": date.strftime('%Y-%m-%d'), "count": 0})
            new_data[res["menu_name"]] = dates

        return new_data

    def __create_model_object(self, result):
        obj = list()

        for res in result:
            temp = QueryObject()

            temp.date = res.date
            temp.count = res.sum

            try:
                temp.menu_name = res.menu_name
            except Exception as e:
                pass

            obj.append(temp)

        return obj

    def for_year(self, year):
        self.__start = year + "-01-01"
        self.__end = year + "-12-31"

        if self.__stats_for == 1:
            return self.__company_query()
        elif self.__stats_for == 2:
            return self.__branch_query()
        elif self.__stats_for == 3:
            return self.__menu_query()

    def for_month(self, year, month):
        self.__start = year + "-" + month + "-01"
        num_days = calendar.monthrange(int(year), int(month))[1]
        self.__end = year + "-" + month + "-" + str(num_days)

        if self.__stats_for == 1:
            return self.__company_query()
        elif self.__stats_for == 2:
            return self.__branch_query()
        elif self.__stats_for == 3:
            return self.__menu_query()

    def for_week(self, year, month, week):
        date_1 = datetime.date(int(year), int(month), 1)
        day = int(date_1.strftime('%w'))
        week = int(week)

        start, end = None, None

        if week == 1:
            end = date_1 + datetime.timedelta(days=6 - day)
        elif week == 2:
            end = date_1 + datetime.timedelta(days=13 - day)
        elif week == 3:
            end = date_1 + datetime.timedelta(days=20 - day)
        elif week == 4:
            end = date_1 + datetime.timedelta(days=27 - day)
        elif week == 5:
            num_days = calendar.monthrange(int(year), int(month))[1]
            end = datetime.date(int(year), int(month), num_days)

        self.__end = end.strftime('%Y-%m-%d')

        if week == 1:
            start = end - datetime.timedelta(days=6 - day)
        elif 2 <= week <= 4:
            start = end - datetime.timedelta(days=6)
        elif week == 5:
            start = end - datetime.timedelta(days=int(end.strftime('%w')))

        self.__start = start.strftime('%Y-%m-%d')

        if self.__stats_for == 1:
            return self.__company_query()
        elif self.__stats_for == 2:
            return self.__branch_query()
        elif self.__stats_for == 3:
            return self.__menu_query()

    def get_start_date(self):
        return self.__start

    def get_end_date(self):
        return self.__end

    def __init__(self, stats_for_id, stats_for):
        self.__stats_for_id = stats_for_id

        """
        stats_for -->
            1 = Company
            2 = Branch
            3 = Menu
        """
        self.__stats_for = stats_for


class FillMissingDates:

    def for_company_and_branch(self, data):
        dates = [datetime.datetime.strptime(d['date'], '%Y-%m-%d') for d in data]

        start_date = datetime.datetime.strptime(self.start_date_str, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(self.end_date_str, '%Y-%m-%d')

        all_dates = [start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days + 1)]

        new_data = []
        for date in all_dates:
            idx = dates.index(date) if date in dates else -1
            if idx != -1:
                new_data.append(data[idx])
            else:
                new_data.append({'date': date.strftime('%Y-%m-%d'), 'count': 0})

        return new_data

    def for_menu(self, data):
        start_date = datetime.datetime.strptime(self.start_date_str, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(self.end_date_str, '%Y-%m-%d')

        for menu in data:
            menu_list = data[menu]
            date_range = [(start_date + datetime.timedelta(days=x)).date() for x in
                          range((end_date - start_date).days + 1)]
            new_menu_list = []
            for date in date_range:
                count = sum(item['count'] for item in menu_list if item['date'] == date)
                new_menu_list.append({
                    'date': str(date),
                    'count': count
                })
            data[menu] = new_menu_list

        return data

    def __init__(self, start_date_str, end_date_str):
        self.start_date_str = start_date_str
        self.end_date_str = end_date_str
