# !/usr/bin/python
# -*- coding: utf-8 -*-

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    s = set()
    i = n - 1
    while i > -1 and a[i] not in s:
        s.add(a[i])
        i -= 1
    print(i + 1)
