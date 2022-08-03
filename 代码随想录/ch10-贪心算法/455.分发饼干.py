#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#


# @lc code=start
class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """ 
        贪心策略
        优先考虑饼干
        """
        g.sort()
        s.sort()
        res = 0
        for i in range(len(s)):  # 小饼干先喂胃口小的
            if res < len(g) and s[i] >= g[res]:
                res += 1
        return res


# @lc code=end
