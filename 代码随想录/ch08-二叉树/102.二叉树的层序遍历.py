#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
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

    def levelOrder(self, root):
        """ 
        二叉树层序遍历  - 迭代法
        使用队列先进先出
        """
        results = []
        if not root:
            return results
        level = [root]
        while root and level:
            results.append([node.val for node in level])
            level = [kid for node in level for kid in (node.left, node.right) if kid]

        return results


# @lc code=end
