#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#


# @lc code=start
class MyQueue:

    def __init__(self):
        """ 
        list实现单调队列
        从大到小
        考虑时间限制
        """

        self.queue = []

    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.pop(0)

    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        # 新元素入队
        self.queue.append(value)

    def front(self):
        """
        返回当前队列的最大值
        """
        return self.queue[0]


class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """ 
        单调队列实现
        """
        que = MyQueue()
        res = []  # 结果存放数组
        for i in range(k):  # 前k个元素处理
            que.push(nums[i])

        res.append(que.front())  # 前k个元素的最大值

        for i in range(k, len(nums)):
            que.pop(nums[i - k])  # 滑动窗口移除前面的元素
            que.push(nums[i])  # 滑动窗口加入最后面的元素
            res.append(que.front())  # 记录对应的最大值

        return res


# @lc code=end

# 超时
# def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#     """
#         单调队列
#         """
#     # 数据为空
#     if not nums or not k:
#         return []

#     if len(nums) == 1:
#         return [nums[0]]

#     # 初始化队列和结果 队列存放数组的下标
#     queue = []
#     res = []

#     for i in range(len(nums)):
#         # 如果当前队列最左侧存放的下标的值等于i-k的值，代表当前队列已满
#         # 但是新元素需要进来，所以列表最左侧的下标出队列
#         if queue and queue[0] == i - k:
#             queue.pop(0)

#         # 对于新进去的元素，如果队列前的数比它小，前面的队列需要出队
#         while queue and nums[queue[-1]] < nums[i]:
#             queue.pop()
#         # 新元素入队
#         queue.append(i)
#         # 当前最大值加入结果数组中
#         if i >= k - 1:
#             res.append(nums[queue[0]])
#     return res
