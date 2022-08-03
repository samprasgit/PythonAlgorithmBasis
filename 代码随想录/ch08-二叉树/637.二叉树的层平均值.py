#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        if not root:
            return res
        quene = deque([root])

        while quene:
            sums = 0
            for _ in range(len(quene)):
                node = quene.popleft()
                sums += node.val
                if node.left:
                    quene.append(node.left)
                if node.right:
                    quene.append(node.right)

            res.append(sums / len(quene))  # 均值

        return res


# @lc code=end
