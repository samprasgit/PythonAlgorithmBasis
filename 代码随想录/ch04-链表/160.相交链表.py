#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 快慢指针
        if headA is None or headB is None:
            return None
        # 两个指针代替 A B
        slow, fast = headA, headB
        while slow != fast:
            slow = slow.next if slow else headB  # 如果A走完了，切换到B走
            fast = fast.next if fast else headA  # 同理切换到B走

        return slow


# @lc code=end
