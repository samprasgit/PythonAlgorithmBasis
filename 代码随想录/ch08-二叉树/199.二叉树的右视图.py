#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """ 
        deque时间复杂度O(1)  list时间复杂度O(n)
        """
        from collections import deque
        res = []
        if not root:
            return res
        quene = deque([root])
        while quene:
            # 每次获取最后一个Node
            node = quene[-1]
            res.append(node.val)
            # 遍历下一层所有的节点
            for _ in range(len(quene)):

                node = quene.popleft()
                if node.left:
                    quene.append(node.left)
                if node.right:
                    quene.append(node.right)

        return res


# @lc code=end
