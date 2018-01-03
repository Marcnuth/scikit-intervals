from .basic_interval import Interval


class FloatInterval(Interval):

    value_type = float

    def _is_element_valid(self, ele):
        return isinstance(ele, (int, float))