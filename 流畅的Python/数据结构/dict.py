# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Time    :   2022/07/26 18:53:55
@Desc    :   字典
"""

# 散列表
tt = (1, 2, (30, 40))
print(hash(tt))  # 3907003130834322577
t1 = (1, 2, [30, 40])
print(hash(t1))
# TypeError: unhashable type: 'list'