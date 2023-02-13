from rstyleslice import rslice, rindex


a = rslice('123456789')
b = rslice(b'123456789')
c = rslice(list('123456789'))
d = rslice(tuple('123456789'))
e = rslice(range(len('123456789')))

# 索引等值
s = [int(x) for x in '123456789']
for i in s:
    assert type(b[i]) is bytes
    assert a[i] == b[i].decode() == c[i] == d[i]
    assert a[-i] == b[-i].decode() == c[-i] == d[-i]

# 切片等值
s = list(range(-15, 16)) + [None]
dt = list(range(1, 16)) + [None]
for start in s:
    for stop in s:
        for step in dt:
            key = slice(start, stop, step)
            assert type(b[key]) is bytes
            assert a[key] == b[key].decode() == ''.join(c[key]) == ''.join(d[key])
            assert len(a[key]) == len(b[key]) == len(c[key]) == len(d[key])
            assert a.getitemSlice(key) == e.getitemSlice(key)
            assert a.setitemSlice(key) == e.setitemSlice(key)

# 正索引取值
assert a[1] == '1'
assert a[2] == '2'
assert a[3] == '3'
assert a[4] == '4'
assert a[5] == '5'
assert a[6] == '6'
assert a[7] == '7'
assert a[8] == '8'
assert a[9] == '9'

assert b[1] == b'1'
assert b[2] == b'2'
assert b[3] == b'3'
assert b[4] == b'4'
assert b[5] == b'5'
assert b[6] == b'6'
assert b[7] == b'7'
assert b[8] == b'8'
assert b[9] == b'9'

# 负索引取值
assert a[-1] == '9'
assert a[-2] == '8'
assert a[-3] == '7'
assert a[-4] == '6'
assert a[-5] == '5'
assert a[-6] == '4'
assert a[-7] == '3'
assert a[-8] == '2'
assert a[-9] == '1'

assert b[-1] == b'9'
assert b[-2] == b'8'
assert b[-3] == b'7'
assert b[-4] == b'6'
assert b[-5] == b'5'
assert b[-6] == b'4'
assert b[-7] == b'3'
assert b[-8] == b'2'
assert b[-9] == b'1'

# 正向切片
assert (a[:] == a[1:9] == a[1:-1] == a[-9:-1] == a[-9:9]
             == a[:9] == a[:-1] == a[1:] == a[-9:] == a[0:9] == a[0:-1]
             == a[1:15] == a[-9:15] == a[:15] == a[0:15]
             == '123456789')
assert a[2:8] == a[2:-2] == a[-8:-2] == a[-8:8] == '2345678'
assert a[3:7] == a[3:-3] == a[-7:-3] == a[-7:7] == '34567'
assert a[4:6] == a[4:-4] == a[-6:-4] == a[-6:6] == '456'
assert a[5:5] == a[5:-5] == a[-5:-5] == a[-5:5] == '5'

# 逆向切片
assert (a[9:1] == a[-1:1] == a[-1:-9] == a[9:-9]
             == a[9:0] == a[-1:0]
             == a[15:1] == a[15:-9] == a[15:0]
             == '987654321')
assert a[8:2] == a[-2:2] == a[-2:-8] == a[8:-8] == '8765432'
assert a[7:3] == a[-3:3] == a[-3:-7] == a[7:-7] == '76543'
assert a[6:4] == a[-4:4] == a[-4:-6] == a[6:-6] == '654'

# 正向切片 + 跳跃
## 2步
assert (a[::2] == a[1:9:2] == a[1:-1:2] == a[-9:-1:2] == a[-9:9:2]
             == a[:9:2] == a[:-1:2] == a[1::2] == a[-9::2] == a[0:9:2] == a[0:-1:2]
             == a[1:15:2] == a[-9:15:2] == a[:15:2] == a[0:15:2]
             == '13579')
assert a[2:8:2] == a[2:-2:2] == a[-8:-2:2] == a[-8:8:2] == '2468'
assert a[3:7:2] == a[3:-3:2] == a[-7:-3:2] == a[-7:7:2] == '357'
assert a[4:6:2] == a[4:-4:2] == a[-6:-4:2] == a[-6:6:2] == '46'
assert a[5:5:2] == a[5:-5:2] == a[-5:-5:2] == a[-5:5:2] == '5'
## 3步
assert (a[::3] == a[1:9:3] == a[1:-1:3] == a[-9:-1:3] == a[-9:9:3]
             == a[:9:3] == a[:-1:3] == a[1::3] == a[-9::3] == a[0:9:3] == a[0:-1:3]
             == a[1:15:3] == a[-9:15:3] == a[:15:3] == a[0:15:3]
             == '147')
assert a[2:8:3] == a[2:-2:3] == a[-8:-2:3] == a[-8:8:3] == '258'
assert a[3:7:3] == a[3:-3:3] == a[-7:-3:3] == a[-7:7:3] == '36'
assert a[4:6:3] == a[4:-4:3] == a[-6:-4:3] == a[-6:6:3] == '4'
assert a[5:5:3] == a[5:-5:3] == a[-5:-5:3] == a[-5:5:3] == '5'
## 4步
assert (a[::4] == a[1:9:4] == a[1:-1:4] == a[-9:-1:4] == a[-9:9:4]
             == a[:9:4] == a[:-1:4] == a[1::4] == a[-9::4] == a[0:9:4] == a[0:-1:4]
             == a[1:15:4] == a[-9:15:4] == a[:15:4] == a[0:15:4]
             == '159')
assert a[2:8:4] == a[2:-2:4] == a[-8:-2:4] == a[-8:8:4] == '26'
assert a[3:7:4] == a[3:-3:4] == a[-7:-3:4] == a[-7:7:4] == '37'
assert a[4:6:4] == a[4:-4:4] == a[-6:-4:4] == a[-6:6:4] == '4'
assert a[5:5:4] == a[5:-5:4] == a[-5:-5:4] == a[-5:5:4] == '5'

# 逆向切片 + 跳跃
## 2步
assert (a[9:1:2] == a[-1:1:2] == a[-1:-9:2] == a[9:-9:2]
             == a[9:0:2] == a[-1:0:2]
             == a[15:1:2] == a[15:-9:2] == a[15:0:2]
             == '97531')
assert a[8:2:2] == a[-2:2:2] == a[-2:-8:2] == a[8:-8:2] == '8642'
assert a[7:3:2] == a[-3:3:2] == a[-3:-7:2] == a[7:-7:2] == '753'
assert a[6:4:2] == a[-4:4:2] == a[-4:-6:2] == a[6:-6:2] == '64'
## 3步骤
assert (a[9:1:3] == a[-1:1:3] == a[-1:-9:3] == a[9:-9:3]
             == a[9:0:3] == a[-1:0:3]
             == a[15:1:3] == a[15:-9:3] == a[15:0:3]
             == '963')
assert a[8:2:3] == a[-2:2:3] == a[-2:-8:3] == a[8:-8:3] == '852'
assert a[7:3:3] == a[-3:3:3] == a[-3:-7:3] == a[7:-7:3] == '74'
assert a[6:4:3] == a[-4:4:3] == a[-4:-6:3] == a[6:-6:3] == '6'

# 赋值
## list
c = rslice([1, 2, 3, 4, 5, 6, 7, 8, 9])
c[1] = 'a'
assert c.core == ['a', 2, 3, 4, 5, 6, 7, 8, 9]
c[9] = 'b'
assert c.core == ['a', 2, 3, 4, 5, 6, 7, 8, 'b']
c[-1] = 'e'
assert c.core == ['a', 2, 3, 4, 5, 6, 7, 8, 'e']
c[-9] = 'e'
assert c.core == ['e', 2, 3, 4, 5, 6, 7, 8, 'e']
c[4:6] = ['44', '55']
assert c.core == ['e', 2, 3, '44', '55', 7, 8, 'e']
c[4:6] = []
assert c.core == ['e', 2, 3, 8, 'e']
c[4:] = [1, 2, 3, 4, 5]
assert c.core == ['e', 2, 3, 1, 2, 3, 4, 5]
c[4:100] = ['1', 2, 3, 4, 5]
assert c.core == ['e', 2, 3, '1', 2, 3, 4, 5]
c[4:] = []
assert c.core == ['e', 2, 3]
c[:] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert c.core == [1, 2, 3, 4, 5, 6, 7, 8, 9]
c[-4:7] = ['44', '55']
assert c.core == [1, 2, 3, 4, 5, '44', '55', 8, 9]
c[-4:] = ['44', '55']
assert c.core == [1, 2, 3, 4, 5, '44', '55']
c[-1:] = [7, 8, 9]
assert c.core == [1, 2, 3, 4, 5, '44', 7, 8, 9]
c[9:] = [7, 8, 9]
assert c.core == [1, 2, 3, 4, 5, '44', 7, 8, 7, 8, 9]
c[-2:] = [7, 8, 9]
assert c.core == [1, 2, 3, 4, 5, '44', 7, 8, 7, 7, 8, 9]
c[1:2] = [9, 8, 7]
assert c.core == [9, 8, 7, 3, 4, 5, '44', 7, 8, 7, 7, 8, 9]
c[1:] = ['9', 8, '7']
assert c.core == ['9', 8, '7']
c[0:] = ['99', 8, '97']
assert c.core == ['99', 8, '97']
c[:0] = ['2', 2, '22']
assert c.core == ['2', 2, '22', '99', 8, '97']
c[:3] = ['32', 32, '232']
assert c.core == ['32', 32, '232', '99', 8, '97']
c[4:-3] = ['p', 3552, '2p32']
assert c.core == ['32', 32, '232', 'p', 3552, '2p32', 8, '97']
c[:-3] = ['qp', 35452, '2pw32']
assert c.core == ['qp', 35452, '2pw32', 8, '97']
c[0:0] = ['q-p', 3547752, '2pw3-2']
assert c.core == ['q-p', 3547752, '2pw3-2', 'qp', 35452, '2pw32', 8, '97']
c[100:99] = ['q-p', 3547752, '2pw3-2']
assert c.core == ['q-p', 3547752, '2pw3-2', 'qp', 35452, '2pw32', 8, '97', 'q-p', 3547752, '2pw3-2']

## tuple
c = rslice((1, 2, 3, 4, 5, 6, 7, 8, 9))
c[1] = 'a'
assert c.core == ('a', 2, 3, 4, 5, 6, 7, 8, 9)
c[9] = 'b'
assert c.core == ('a', 2, 3, 4, 5, 6, 7, 8, 'b')
c[-1] = 'e'
assert c.core == ('a', 2, 3, 4, 5, 6, 7, 8, 'e')
c[-9] = 'e'
assert c.core == ('e', 2, 3, 4, 5, 6, 7, 8, 'e')
c[4:6] = ('44', '55')
assert c.core == ('e', 2, 3, '44', '55', 7, 8, 'e')
c[4:6] = tuple()
assert c.core == ('e', 2, 3, 8, 'e')
c[4:] = (1, 2, 3, 4, 5)
assert c.core == ('e', 2, 3, 1, 2, 3, 4, 5)
c[4:100] = ('1', 2, 3, 4, 5)
assert c.core == ('e', 2, 3, '1', 2, 3, 4, 5)
c[4:] = tuple()
assert c.core == ('e', 2, 3)
c[:] = (1, 2, 3, 4, 5, 6, 7, 8, 9)
assert c.core == (1, 2, 3, 4, 5, 6, 7, 8, 9)
c[-4:7] = ('44', '55')
assert c.core == (1, 2, 3, 4, 5, '44', '55', 8, 9)
c[-4:] = ('44', '55')
assert c.core == (1, 2, 3, 4, 5, '44', '55')
c[-1:] = (7, 8, 9)
assert c.core == (1, 2, 3, 4, 5, '44', 7, 8, 9)
c[9:] = (7, 8, 9)
assert c.core == (1, 2, 3, 4, 5, '44', 7, 8, 7, 8, 9)
c[-2:] = (7, 8, 9)
assert c.core == (1, 2, 3, 4, 5, '44', 7, 8, 7, 7, 8, 9)
c[1:2] = (9, 8, 7)
assert c.core == (9, 8, 7, 3, 4, 5, '44', 7, 8, 7, 7, 8, 9)
c[1:] = ('9', 8, '7')
assert c.core == ('9', 8, '7')
c[0:] = ('99', 8, '97')
assert c.core == ('99', 8, '97')
c[:0] = ('2', 2, '22')
assert c.core == ('2', 2, '22', '99', 8, '97')
c[:3] = ('32', 32, '232')
assert c.core == ('32', 32, '232', '99', 8, '97')
c[4:-3] = ('p', 3552, '2p32')
assert c.core == ('32', 32, '232', 'p', 3552, '2p32', 8, '97')
c[:-3] = ('qp', 35452, '2pw32')
assert c.core == ('qp', 35452, '2pw32', 8, '97')
c[0:0] = ('q-p', 3547752, '2pw3-2')
assert c.core == ('q-p', 3547752, '2pw3-2', 'qp', 35452, '2pw32', 8, '97')
c[100:99] = ('q-p', 3547752, '2pw3-2')
assert c.core == ('q-p', 3547752, '2pw3-2', 'qp', 35452, '2pw32', 8, '97', 'q-p', 3547752, '2pw3-2')

## str
a = rslice('123456789')
a[1] = 'a'
assert a.core == 'a23456789'
a[9] = 'i'
assert a.core == 'a2345678i'
a[5] = 'e'
assert a.core == 'a234e678i'
a[-1] = 'r'
assert a.core == 'a234e678r'
a[-9] = 'x'
assert a.core == 'x234e678r'
a[-5] = 'w'
assert a.core == 'x234w678r'
a[2:4] = 'inm'
assert a.core == 'xinmw678r'
a[2:4] = ''
assert a.core == 'xw678r'
a[2:4] = 'plok'
assert a.core == 'xplok8r'
a[2:2] = '95'
assert a.core == 'x95lok8r'
a[6:3] = 'ijng'
assert a.core == 'x9ijng8r'
a[6:-3] = 'qwer'
assert a.core == 'x9ijnqwer8r'
a[6:-2] = 'zxcv'
assert a.core == 'x9ijnzxcvr'
a[6:] = 'asdf'
assert a.core == 'x9ijnasdf'
a[-3:] = 'poiu'
assert a.core == 'x9ijnapoiu'
a[:3] = 'poiu'
assert a.core == 'poiujnapoiu'
a[:-5] = 'lkjh'
assert a.core == 'lkjhpoiu'
a[:0] = 'qwer'
assert a.core == 'qwerlkjhpoiu'
a[:1000] = '123456789'
assert a.core == '123456789'
a[1:1000] = 'a123456789a'
assert a.core == 'a123456789a'
a[0:1000] = 'b123456789e'
assert a.core == 'b123456789e'
a[20:21] = 'poiu'
assert a.core == 'b123456789epoiu'
a[30:30] = '-poiu'
assert a.core == 'b123456789epoiu-poiu'
a[130:90] = '+poiu'
assert a.core == 'b123456789epoiu-poiu+poiu'
a[0:0] = '+poiu'
assert a.core == '+poiub123456789epoiu-poiu+poiu'
a[5:1000] = '123456'
assert a.core == '+poi123456'
assert rslice('123456789')[-1:] == '9'

## bytes
a = rslice(b'123456789')
a[1] = b'a'
assert a.core == b'a23456789'
a[9] = b'i'
assert a.core == b'a2345678i'
a[5] = b'e'
assert a.core == b'a234e678i'
a[-1] = b'r'
assert a.core == b'a234e678r'
a[-9] = b'x'
assert a.core == b'x234e678r'
a[-5] = b'w'
assert a.core == b'x234w678r'
a[2:4] = b'inm'
assert a.core == b'xinmw678r'
a[2:4] = b''
assert a.core == b'xw678r'
a[2:4] = b'plok'
assert a.core == b'xplok8r'
a[2:2] = b'95'
assert a.core == b'x95lok8r'
a[6:3] = b'ijng'
assert a.core == b'x9ijng8r'
a[6:-3] = b'qwer'
assert a.core == b'x9ijnqwer8r'
a[6:-2] = b'zxcv'
assert a.core == b'x9ijnzxcvr'
a[6:] = b'asdf'
assert a.core == b'x9ijnasdf'
a[-3:] = b'poiu'
assert a.core == b'x9ijnapoiu'
a[:3] = b'poiu'
assert a.core == b'poiujnapoiu'
a[:-5] = b'lkjh'
assert a.core == b'lkjhpoiu'
a[:0] = b'qwer'
assert a.core == b'qwerlkjhpoiu'
a[:1000] = b'123456789'
assert a.core == b'123456789'
a[1:1000] = b'a123456789a'
assert a.core == b'a123456789a'
a[0:1000] = b'b123456789e'
assert a.core == b'b123456789e'
a[20:21] = b'poiu'
assert a.core == b'b123456789epoiu'
a[30:30] = b'-poiu'
assert a.core == b'b123456789epoiu-poiu'
a[130:90] = b'+poiu'
assert a.core == b'b123456789epoiu-poiu+poiu'
a[0:0] = b'+poiu'
assert a.core == b'+poiub123456789epoiu-poiu+poiu'
a[5:1000] = b'123456'
assert a.core == b'+poi123456'

# __getattr__
assert rslice('abcd').count('a') == 1
assert rslice('abcd').index('b') == 1
assert rslice('abcd').index_('b') == 2
assert rslice('ABCd').lower() == 'abcd'
assert rslice('ABCd').lower().count('a') == 1
a = rslice([6,7,8,9])
b = rslice([6,7,8,9])
c = rslice([6,7,8,9])
d = rslice([6,7,8,9])
assert a.pop(1) == 7
assert b.pop(rindex(1)) == 6
assert c.pop_(1) == 8
assert c.pop_(rindex(1)) == 7

print('\n测试通过')