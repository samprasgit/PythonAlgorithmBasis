#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
# 单链表


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # 虚拟节点

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        for _ in range(index + 1):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtHead(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtTail(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:

        if index > self.size:
            return

        if index < 0:
            index = 0

        #  计算累加
        self.size += 1

        pred = self.head

        for _ in range(index):
            pred = pred.next

        to_add = ListNode(val)
        to_add.next = pred.next

        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        pred = self.head
        for _ in range(index):
            pred = pred.next

        pred.next = pred.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
