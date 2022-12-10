import calendar
import datetime


class ShyosaiDateTime:

    def __init__(self) -> None:
        pass

    def current_second(self):
        return datetime.datetime.now().second

    def current_minute(self):
        return datetime.datetime.now().minute

    def current_hour(self):
        return datetime.datetime.now().hour

    def current_day(self):
        return datetime.datetime.now().day

    def current_month(self, a_bAsString:bool=False):

        '''
        returns current mounth number of the year;
        returns current mounth name if a_bAsString is true
        '''

        month_number = datetime.datetime.now().month
        if a_bAsString:
            return calendar.month_name[month_number]
        return month_number

    def current_year(self):
        return datetime.datetime.now().year

    def get_month_name(self, a_nMonthNumber:int):
        return calendar.month_name[a_nMonthNumber]

    def days_in_year(self, a_nYear:int):

        '''
        returns count of days in the given year
        '''

        return 365 + calendar.isleap(a_nYear)

    def days_in_month(self, a_nYear:int, a_nMonth:int):
        return calendar.monthrange(a_nYear, a_nMonth)[1]