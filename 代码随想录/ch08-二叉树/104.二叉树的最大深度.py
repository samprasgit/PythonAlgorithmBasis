# @before-stub-for-debug-begin
from python3problem104 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
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

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """ 
        二叉树层序遍历
        """
        if not root:
            return 0
        results = []
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

            results.append(res)

        return len(results)


# @lc code=end
