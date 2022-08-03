#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
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

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        results = []
        if not root:
            return results
        quene = deque([root])
        while quene:
            res = []
            for _ in range(len(quene)):
                node = quene.popleft()
                res.append(node.val)
                if node.left:
                    quene.append(node.left)
                if node.right:
                    quene.append(node.right)

            results.append(max(res))

        return results


# @lc code=end
