# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    :   2022/07/25 10:27:52
@Desc    :   None
"""

# 元组拆包
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates  # 元组拆包
print(latitude)
print(longitude)

# 用*运算把一个可迭代对象拆开作为函数的参数
t = (20, 8)
quotient, remainder = divmod(*t)
print(quotient, remainder)  # 2, 4

# *args 来获取不确定数量的参数
a, b, *res = range(5)

print(a, b, res)  # 0 1 [2, 3, 4]

# 嵌套元组拆包
metro_areas = [('Tokyo', 'JP', 36.933, (35, 139)), ('Delhi NCR', 'IN', 21, (28, 77)), ('Mexico City', 'MX', 20, (19, -99)), ('New York-Newark', 'Us', 20, (40, -74)),
               ('Sao Paulo', 'BR', 19, (-23, -46))]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:  # ➋
    if longitude <= 0:  # ➌
        print(fmt.format(name, latitude, longitude))
#                 |   lat.    |   long.
# Mexico City     |   19.0000 |  -99.0000
# New York-Newark |   40.0000 |  -74.0000
# Sao Paulo       |  -23.0000 |  -46.0000

# 具名元组
# namedstuple
# 创建一个具名元组需要两个参数，一个是类名，一个是类的各个字段的名字
# 专有属性
# _fields 类属性  一个包含这个类所有字段名称的元组
# 类方法  _make(iterable)  通过接受一个可迭代对象来生成这个类的一个实例
# 实例方法 _asdict()  把具名元组以 collections.OrderedDict 的形式返回

from collections import namedtuple

City = namedtuple('City', 'name country polulation coordinates')
tokyo = City('Tokyo', 'JP', 36, (35, 139))

print(tokyo)
# City(name='Tokyo', country='JP', polulation=36, coordinates=(35, 139))

print(tokyo.polulation)  # 36
print(tokyo.coordinates)  # (35, 139)

print(City._fields)
# ('name', 'country', 'polulation', 'coordinates')

print()