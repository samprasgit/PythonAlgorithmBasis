#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
from tracemalloc import start


class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        """ 
        剪枝的回溯算法
        """
        res = []  # 存放符合条件结果的结合
        path = []  # 存放符合条件结果

        def backtrack(n, k, startIndex):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(startIndex, n - (k - len(path)) + 2):  # 优化剪枝的地方
                path.append(i)  #处理节点
                backtrack(n, k, i + 1)  # 递归
                path.pop()  # 回溯，撤销处理的节点

        backtrack(n, k, 1)
        return res


# @lc code=end
