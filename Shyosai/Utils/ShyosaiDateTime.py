import calendar
import datetime


class ShyosaiDateTime:

    def __init__(self) -> None:
        pass
    
    # Public

    def currentSecond(self):
        return datetime.datetime.now().second

    def currentMinute(self):
        return datetime.datetime.now().minute

    def currentHour(self):
        return datetime.datetime.now().hour

    def currentDay(self):
        return datetime.datetime.now().day

    def currentMonth(self, a_bAsString:bool=False):

        '''
        returns current mounth number of the year;
        returns current mounth name if a_bAsString is true
        '''

        month_number = datetime.datetime.now().month
        if a_bAsString:
            return calendar.month_name[month_number]
        return month_number

    def currentYear(self):
        return datetime.datetime.now().year

    def getMonthName(self, a_nMonthNumber:int):
        return calendar.month_name[a_nMonthNumber]

    def daysInYear(self, a_nYear:int):

        '''
        returns count of days in the given year
        '''

        return 365 + calendar.isleap(a_nYear)

    def daysInMonth(self, a_nYear:int, a_nMonth:int):
        return calendar.monthrange(a_nYear, a_nMonth)[1]

