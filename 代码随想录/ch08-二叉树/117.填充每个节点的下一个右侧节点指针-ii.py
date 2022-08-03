#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:

    def connect(self, root: 'Node') -> 'Node':
        """ 
        层序遍历
        """
        if not root:
            return None
        quene = deque([root])
        while quene:

            tail = None  # 维护每一层的尾节点
            for i in range(len(quene)):
                node = quene.popleft()
                if tail:
                    tail.next = node  # 尾节点指向当前节点

                tail = node

                if node.left:
                    quene.append(node.left)
                if node.right:
                    quene.append(node.right)

        return root


# @lc code=end
