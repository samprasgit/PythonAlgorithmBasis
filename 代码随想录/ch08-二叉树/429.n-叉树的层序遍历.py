#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        results = []
        if not root:
            return results
        quene = deque([root])

        while quene:
            res = []
            for _ in range(len(quene)):
                node = quene.popleft()
                res.append(node.val)
                if node.children:
                    quene.extend(node.children)

            results.append(res)

        return results


# @lc code=end
