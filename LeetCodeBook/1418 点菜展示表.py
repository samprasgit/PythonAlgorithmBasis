# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :   1418 点菜展示表.py
@Time    :   2021/07/06 19:46:57
@Desc    :   None
"""

from collections import defaultdict


class Solution:
    def display(self, orders):
        ret = []
        foods = set()
        table_into = defaultdict(lambda: defaultdict(int))

        for _, table, food in orders:
            table_into[table][food] += 1
            foods.add(food)

        foods = sorted(foods)
        # 组装表头
        ret.append(["Table"] + foods)
        # 根据int(table)进行排序
        for table_num in sorted(table_into, key=lambda x: int(x)):
            tmp = [table_num]
            # 循环实物，查找该桌是否点了此食物
            for food in foods:
                tmp.append(str(table_into.get(table_num).get(food, 0)))

            ret.append(tmp)

        return ret
