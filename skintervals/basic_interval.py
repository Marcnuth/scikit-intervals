from abc import ABC, abstractmethod
import numpy as np

class Interval(ABC):

    value_type = None

    def __init__(self, lower, upper, include_lower, include_upper):
        self.lower, self.include_lower = lower, include_lower
        self.upper, self.include_upper = upper, include_upper

        # element type validation & brackets validation
        assert self.lower != np.inf, 'lower value could not be inf'
        assert self.upper != -np.inf, 'upper value could not be -inf'

        assert self._is_element_valid(self.lower) if self.lower != -np.inf else not self.include_lower, 'lower value is invalid'
        assert self._is_element_valid(self.upper) if self.upper != np.inf else not self.include_upper, 'upper value is invalid'

        # interval validation:
        pass_when_same_value = (self.upper == self.lower and self.include_upper and self.include_lower)
        pass_when_diff_value = (self.upper != np.inf and self.lower != -np.inf and self.upper > self.lower)
        pass_when_having_inf = (self.upper == np.inf or self.lower == -np.inf)
        assert pass_when_diff_value or pass_when_same_value or pass_when_having_inf, 'the interval values are invalid'


    def __lt__(self, other):
        # (1, 3) < [3, 9), (1, 3) < (3, 9), (1, 2) < (3, 9)
        if self.upper == np.inf or other.lower == -np.inf:
            return False
        else:
            return self.upper < other.lower or (self.upper == other.lower and not self.include_upper)

    def __le__(self, other):
        # (1, 3] <= [3, 9)
        if self.upper == np.inf or other.lower == -np.inf:
            return False
        else:
            return self.upper <= other.lower

    def __gt__(self, other):
        if self.lower == -np.inf or other.upper == np.inf:
            return False
        else:
            return self.lower > other.upper or (self.lower == other.upper and not other.include_upper)

    def __ge__(self, other):
        if self.lower == -np.inf or other.upper == np.inf:
            return False
        else:
            return self.lower >= other.upper

    def __eq__(self, other):
        return self.lower == other.lower and self.upper == other.upper and \
               self.include_lower == other.include_lower and self.include_upper == other.include_upper

    def __ne__(self, other):
        return not self.__eq__(other=other)

    def __str__(self):
        left_brackets, right_brackets = ['(', '['], [')', ']']
        return '{}{},{}{}'.format(left_brackets[self.include_lower],
                                  '' if self.lower == -np.inf else self._element_to_str(self.lower),
                                  '' if self.upper == np.inf else self._element_to_str(self.upper),
                                  right_brackets[self.include_upper])

    def __contains__(self, key):
        if isinstance(key, self.value_type):
            return self._contains_element(key)
        elif isinstance(key, Interval):
            return self._contains_interval(key)
        else:
            raise ValueError('the parameter should be type of %s or Interval' % self.value_type)

    def _contains_interval(self, other):
        return self.intersection(other) == other

    def _contains_element(self, ele):
        is_under_upper = (self.upper == np.inf) or ele < self.upper
        is_above_lower = (self.lower == -np.inf) or ele > self.lower
        if is_under_upper and is_above_lower:
            return True

        if ele == self.upper and self.include_upper:
            return True

        if ele == self.lower and self.include_lower:
            return True

        return False

    def _is_element_valid(self, ele):
        return True

    def _element_to_str(self, ele):
        return str(ele)

    @classmethod
    def _str_to_element(cls, ele_str):
        return cls.value_type(ele_str)

    def intersection(self, other):
        assert type(self) == type(other), 'two intervals must be the same type'
        # special handling
        if other < self or other > self:
            return None
        elif other == self:
            return other

        # find upper and upper_boundary
        if self.upper == np.inf:
            new_upper, new_include_upper = other.upper, other.include_upper
        elif other.upper == np.inf:
            new_upper, new_include_upper = self.upper, self.include_upper
        elif other.upper == self.upper:
            new_upper, new_include_upper = other.upper, other.include_upper and self.include_upper
        elif other.upper < self.upper:
            new_upper, new_include_upper = other.upper, other.include_upper
        else:
            new_upper, new_include_upper = self.upper, self.include_upper

        # find lower and lower_boundary
        if self.lower == -np.inf:
            new_lower, new_include_lower = other.lower, other.include_lower
        elif other.lower == -np.inf:
            new_lower, new_include_lower = self.lower, self.include_lower
        elif other.lower == self.lower:
            new_lower, new_include_lower = other.lower, other.include_lower and self.include_lower
        elif other.lower < self.lower:
            new_lower, new_include_lower = self.lower, self.include_lower
        else:
            new_lower, new_include_lower = other.lower, other.include_lower

        return self.__class__(new_lower, new_upper, new_include_lower, new_include_upper)

    @classmethod
    def from_str(cls, interval_string):
        assert len(interval_string) >= 3, 'interval_string should be format of: [\[\(][^,]*,[^,]*[\]\)]'

        char_lower, char_upper = interval_string[0], interval_string[-1]
        assert char_lower in ['[', '('], 'invalid lower bracket, please use [ or ('
        assert char_upper in [']', ')'], 'invalid upper barcket, please use ] or )'

        try:
            parts = interval_string[1:-1].split(',')
            return cls(lower=cls._str_to_element(parts[0]) if parts[0].strip() else -np.inf,
                       upper=cls._str_to_element(parts[1]) if parts[1].strip() else np.inf,
                       include_lower=(char_lower == '['), include_upper=(char_upper == ']'))
        except AssertionError as e:
            raise e
        except Exception as e:
            raise ValueError('the string cannot be recognized, please check it. error message: %s' % e)

    def to_str(self):
        return self.__str__()

