# Introduction
Scikit-intervals is a library for handling intervals in python, and this library support both number interval and datetime interval.
Comparing to other library, this lib is more advanced in:
- use numpy's infinite as the infinite boundary instead of other infinite library, which is more easy for engineer especailly for data science engineer
- completely support converting interval to string, or converting string to interval, which will good for persistence and storage
- support both number interval and datetime interval

# Install

```shell

pip install scikit-intervals

```

# Usage

## Initializing an interval

### Initializing from string

```python

from skintervals import DatetimeInterval, FloatInterval

# interval for datetime in (2017-05-12 00:00:00, 2018-01-01 12:00:39]
inter1 = DatetimeInterval.from_str('(2017-05-12, 2018-01-01 12:00:39]')

# interval for number in (1.0, 3.0)
inter2 = FloatInterval.from_str('(1,3)')

# interval for number which is smaller than 5.4
inter3 = FloatInterval.from_str('(5.4)')

# interval for number in whole R
inter4 = FloatInterval.from_str('(,)')
```


