# !/usr/bin/python
# -*- coding: utf-8 -*-


class Solution:
    def peakIndexInMountainArray(self, arr):
        # 枚举法  找到下标 arr_i>arr_{i+1}
        n = len(arr)
        res = -1
        for i in range(1, n - 1):
            if arr[i] > arr[i + 1]:
                res = i
                break
        return res


class Solution2:
    def peakIndexInMountainArray(self, arr):
        # 二分查找
        n = len(arr)
        left, right, res = 1, n - 1, 0
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
