class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        while L < R:
            Mid = (L + R) // 2
            if nums[Mid] < nums[Mid + 1]:
                L = Mid + 1
            else:
                R = Mid
        return L
         