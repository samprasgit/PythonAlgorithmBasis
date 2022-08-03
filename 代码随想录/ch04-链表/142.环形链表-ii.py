#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def detectCycle(self, head: ListNode) -> ListNode:
        # 快慢指针
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            # 如果相遇
            if slow == fast:
                fast = head

                while fast != slow:
                    slow = slow.next
                    fast = fast.next

                return fast

        return None


# @lc code=end
