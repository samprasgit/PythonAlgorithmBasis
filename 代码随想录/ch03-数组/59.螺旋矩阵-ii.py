#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
from tracemalloc import start


class Solution:

    def generateMatrix(self, n: int) -> List[List[int]]:
        # 顺时针模拟
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0  # 起始点
        loop = n // 2  # 循环的次数
        mid = n // 2  # 矩阵的中心点
        count = 1  # 计数

        for offset in range(1, loop + 1):  # 每循环一次偏移量+1，偏移量从1开始
            # 从左到右
            for i in range(starty, n - offset):
                nums[startx][i] = count
                count += 1
            # 从上到下
            for i in range(startx, n - offset):
                nums[i][n - offset] = count
                count += 1

            # 从右到左
            for i in range(n - offset, starty, -1):
                nums[n - offset][i] = count
                count += 1

            # 从下到上
            for i in range(n - offset, startx, -1):
                nums[i][starty] = count
                count += 1

            # 更新起点
            startx += 1
            starty += 1

        # 当n为奇数时，填充中心点
        if n % 2 != 0:
            nums[mid][mid] = count
        return nums


# @lc code=end
