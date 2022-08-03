#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
from collections import deque


class MyStack:
    """ 
    实用一个队列实现栈
    
    """

    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        """
        元素入栈
        """
        self.que.append(x)

    def pop(self) -> int:
        """ 
        元素出栈
        """
        if self.empty():
            return None
        for i in range(len(self.que) - 1):
            self.que.append(self.que.popleft())

        return self.que.popleft()

    def top(self) -> int:
        """"
        栈顶元素
        
        """
        if self.empty():
            return None
        return self.que[-1]

    def empty(self) -> bool:
        """ 
        返回栈是否为空
        """
        return not self.que


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
