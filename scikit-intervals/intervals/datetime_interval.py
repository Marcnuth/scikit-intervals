from .basic_interval import Interval
from datetime import datetime
import arrow

class DatetimeInterval(Interval):
    value_type = datetime

    def _is_element_valid(self, ele):
        return isinstance(ele, datetime)

    def _element_to_str(self, ele):
        return arrow.get(ele).format('YYYY-MM-DD HH:mm:ss ZZ')

    @classmethod
    def _str_to_element(cls, ele_str):
        return arrow.get(ele_str).naive