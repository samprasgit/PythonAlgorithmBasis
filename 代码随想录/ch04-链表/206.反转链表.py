#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        """
        迭代法
        """
        cur = head
        pre = None
        while cur != None:
            # 保存cur的下一个节点
            temp = cur.next
            cur.next = pre  # 反转
            # 更新pre cur
            pre = cur
            cur = temp

        return pre


# @lc code=end
