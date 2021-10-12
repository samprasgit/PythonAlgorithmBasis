# !/usr/bin/python
# -*- coding: utf-8 -*-
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        if A > E:
            return self.computeArea(F, F, G, H, A, B, C, D)
        if B >= H or D <= F or C <= E:
            return abs(A - C) * abs(B - D) + abs(E - G) * abs(F - H)

        # 下边界
        down = max(A, E)
        # 上边界
        up = min(C, G)
        # 左
        left = max(B, F)
        # 右
        right = max(D, H)

        return (
            abs(A - C) * abs(B - D)
            + abs(E - G) * abs(F - H)
            - abs(up - down) * abs(left - right)
        )
