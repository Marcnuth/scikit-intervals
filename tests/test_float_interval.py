from skintervals import FloatInterval

def test_compare():
    a = FloatInterval.from_str('[1, 3]')
    b = FloatInterval.from_str('(1, 3]')
    c = FloatInterval.from_str('[10.4, 39)')
    d = FloatInterval.from_str('(-1.2, 1)')
    e = FloatInterval.from_str('[10.4, 39)')
    print(a, b, c, d)

    assert a < c and c > a and a != b
    assert d < a and e == c and b in a and 10.5 in c

    f = FloatInterval.from_str('[10.4, )')
    flag = True
    try:
        g = FloatInterval.from_str('[, 15)')
        flag = False
    except:
        print('OK')
        g = FloatInterval.from_str('(, 15)')
    assert flag

    try:
        h = FloatInterval.from_str('( ,]')
        flag = False
    except:
        print('OK')
        h = FloatInterval.from_str('( ,)')
    assert flag
    print(f, g, h)

    assert a in h and f in h and g in h and h in h and a in a
    assert not a < h and c in f

    assert (g.intersection(c)) == FloatInterval.from_str('[10.4,15.0)')
    assert (f.intersection(c)) == FloatInterval.from_str('[10.4,39.0)')