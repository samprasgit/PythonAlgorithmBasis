# !/usr/bin/python
# -*- coding: utf-8 -*-

from re import L
from readline import append_history_file


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# -----------------------二叉树的递归遍历-------------------------------------#
# 二叉树前序遍历 - 递归
class Solution:

    def preorder(self, root):
        res = []  # 保存结果

        def traversal(root):
            if not root:
                return None
            res.append(root.val)  # 前序
            traversal(root.left)
            traversal(root.right)

        traversal(root)
        return res


# 二叉树中序遍历 - 递归
class Solution:

    def inorder(self, root):
        res = []  # 保存结果

        def traversal(root):
            if not root:
                return None

            traversal(root.left)
            res.append(root.val)  # 中序
            traversal(root.right)

        traversal(root)
        return res


# 二叉树后序遍历 - 递归
class Solution:

    def postorder(self, root):
        res = []  # 存储结果

        def traversal(root):
            if not root:
                return None
            traversal(root.left)
            traversal(root.right)
            res.append(root.val)

        traversal(root)
        return res


# -----------------------二叉树的迭代遍历-------------------------------------#
# 前序遍历 - 迭代
class Solution:

    def preorder(self, root):
        # 根节点为空，返回空列表
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            # 中节点元素先处理
            res.append(node.val)
            # 右节点先入栈
            if node.right:
                stack.append(node.right)
            # 左节点入栈
            if node.left:
                stack.append(node.left)

        return res


# 中序遍历- 迭代


class Solution:

    def inorder(self, root):
        if not root:
            return []
        stack = []
        res = []
        curr = root

        while cur or stack:
            # 先访问最底层的左子树节点
            if curr:
                stack.append(curr)
                curr = curr.left
            # 到达最左节点处理栈顶节点
            else:
                curr = stack.pop()
                res.append(curr.val)
                # 取栈顶元素右节点
                curr = curr.right

        return res


# 二叉树后序遍历 - 迭代
class Solution:
    """ 
    中右左遍历 返回倒序数组
    """

    def postorder(self, root):
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            # 中节点处理
            res.append(node.val)
            # 左节点先入栈
            if node.left:
                stack.append(node.left)
            # 右节点入栈
            if node.right:
                stack.append(node.right)

        return res[::-1]
