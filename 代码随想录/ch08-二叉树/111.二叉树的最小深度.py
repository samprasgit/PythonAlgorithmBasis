#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
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

    def minDepth(self, root: Optional[TreeNode]) -> int:
        """ 
        层序遍历
        """
        if not root:
            return 0
        # depth = 1  # 根节点深度为1
        quene = deque([(root, 1)])
        while quene:
            node, depth = quene.popleft()

            if not node.left and not node.right:
                return depth
            # 先左子节点，由于左子节点没有孩子，则就是这一层了
            if node.left:
                quene.append((node.left, depth + 1))

            if node.right:
                quene.append((node.right, depth + 1))

        return 0


# @lc code=end
