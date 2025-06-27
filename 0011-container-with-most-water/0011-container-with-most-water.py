class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = []
        L = 0
        R = len(height) - 1
        while L < R:
            Height = min(height[L] , height[R])
            Width = (R - L)
            area.append(Height*Width)
            
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        return max(area)               




        