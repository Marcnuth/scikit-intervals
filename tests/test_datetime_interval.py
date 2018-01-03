from intervals.datetime_interval import DatetimeInterval
import arrow
from pprint import pprint

def test_compare():
    a = DatetimeInterval.from_str('[{}, {}]'.format(arrow.get(2017, 12, 30).format('YYYY-MM-DD'), arrow.get(2017, 12, 31).format('YYYY-MM-DD')))
    b = DatetimeInterval.from_str('(  {}, {}]'.format(arrow.get(2017, 12, 30).format('YYYY-MM-DD'), arrow.get(2017, 12, 31).format('YYYY-MM-DD')))
    c = DatetimeInterval.from_str('[{}, {}]'.format(arrow.get(2017, 5, 30).format('YYYY-MM-DD'), arrow.get(2018, 1, 31).format('YYYY-MM-DD')))
    d = DatetimeInterval.from_str('[{}, {}]'.format(arrow.get(2016, 5, 2).format('YYYY-MM-DD'), arrow.get(2017, 1, 9).format('YYYY-MM-DD')))
    e = DatetimeInterval.from_str('[{}, {})'.format(arrow.get(2017, 5, 30).format('YYYY-MM-DD'), arrow.get(2018, 1, 31).format('YYYY-MM-DD')))
    print(a, b, c, d, e)

    assert a in c and d < c and c > d and c >= d and e in c and a != b
    assert arrow.get(2017, 7, 30).naive in e and arrow.get(2017, 7, 30).naive not in d


    f = DatetimeInterval.from_str('[{}, )'.format(arrow.get(2017, 12, 30).format('YYYY-MM-DD')))
    flag = True
    try:
        g = DatetimeInterval.from_str('[ ,  {}]'.format(arrow.get(2018, 1, 31).format('YYYY-MM-DD')))
        flag = False
    except:
        print('OK')
        g = DatetimeInterval.from_str('( ,  {}]'.format(arrow.get(2018, 1, 31).format('YYYY-MM-DD')))
    assert flag

    h = DatetimeInterval.from_str('( ,)')
    assert flag
    print(f, g, h)

    assert a in h and f in h and g in h and h in h and a in a

    assert not a < h and b in f

    assert (g.intersection(c)) == DatetimeInterval.from_str('[2017-05-30 00:00:00,2018-01-31 00:00:00]')
    assert (f.intersection(c)) == DatetimeInterval.from_str('[2017-12-30 00:00:00,2018-01-31 00:00:00]')
    assert h.intersection(g) == g