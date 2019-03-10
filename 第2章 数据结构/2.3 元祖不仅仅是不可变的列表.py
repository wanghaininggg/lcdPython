# 2.3.1 元祖和记录

# 实例2-7 把元祖用作记录

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
for country, _ in traveler_ids:
    print(country)
print('\n')

# 2.3.2 元祖拆包
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates
print(latitude, longitude)

print(divmod(20, 8))
t = (20, 8)
divmod(*t)
quotient, remainder = divmod(*t)
print(quotient, remainder)
import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename)  # '_' 占位符
print('\n')

a, b, *rest = range(5)
print(a, b, rest)
a, b, *rest = range(2)  # *前缀只能用在一个变量名前面，可以出现在赋值表达式的任意位置
print(a, b, rest)
a, *body, c, d = range(5)
print(a, body, c, d)
*head, b, c, d = range(5)
print(*head, b, c, d)
print('\n')

# 2.3.3嵌套元祖拆包

# 实例 2-8 用嵌套元组来获取精度
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'In', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611,  -74.080386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
print('\n')

# 2.3.4 具名元组

# 实例 2-9 定义和使用具名元组

# 创建一个具名元祖需要两个参数，一个是类名，一个是各个字段的名字，后者可以是由数个字符串组成的可迭代对象。或者是由空格分割开的字段名组成的字符串
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo.name)
print(tokyo.country)

# 示例2-10 具名元祖的属性和方法
print(City._fields)
LatLong = namedtuple('Latlong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)  # _make通过接受一个可迭代对象来生成这个类的一个实例
print(delhi._asdict())



