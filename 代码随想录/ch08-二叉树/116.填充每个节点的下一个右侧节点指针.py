#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start


# Definition for a Node.
class Node:

    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from collections import deque


class Solution:

    def connect(self, root):
        """ 
        层序遍历解法
        """
        if not root:
            return root
        quene = deque([root])
        while quene:
            for i in range(len(quene)):
                # 队首取出元素
                node = quene.popleft()
                # 链接
                if i < len(quene) - 1:
                    node.next = quene[0]
                else:
                    node.next = None
                if node.left:
                    quene.append(node.left)
                if node.right:
                    quene.append(node.right)

        return root


# @lc code=end
