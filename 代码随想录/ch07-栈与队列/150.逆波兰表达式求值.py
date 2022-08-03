#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#


# @lc code=start
class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        """ 
        后缀表达式
        栈：遇到数字入栈，遇到算符则取出栈顶数字进行计算，将结果压入栈中
        """
        stack = []
        for item in tokens:
            if item in tokens:
                if item not in {"+", "-", "*", "/"}:
                    stack.append(item)

                else:
                    first_num, second_num = stack.pop(), stack.pop()
                    stack.append(int(eval(f'{second_num} {item} {first_num}')))

        return int(stack.pop())


# @lc code=end
