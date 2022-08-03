#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:
        # 虚拟头结点
        res = ListNode(next=head)
        pre = res

        # 必须有pre的下一个节点和下下一个节点，否则说明已经交换结束了
        while pre.next and pre.next.next:
            cur = pre.next
            post = pre.next.next

            # pre cur post 对应 最左 当前  最右的节点

            cur.next = post.next
            post.next = cur
            pre.next = post

            pre = pre.next.next

        return res.next


# @lc code=end
