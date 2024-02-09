
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import datetime


class DateTimeUtility:
    @staticmethod
    def get_date_of_birth_from_age(age: int) -> int:
        time_passed = datetime.datetime.now() - relativedelta(years=age)
        return time_passed.year